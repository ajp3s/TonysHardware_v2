from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic as gen_views, View
from storages.backends.s3boto3 import S3Boto3Storage

from TonysHardware_v2.functionality.funcs import get_model_from_model_name, create_modelform
from TonysHardware_v2.validators.custom_validators import ValidateGroupMembershipMixin


class HardwareAddView(gen_views.CreateView, UserPassesTestMixin):
    template_name = 'hardware/add_hardware.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Moderators').exists()

    def get_form_class(self):
        model = self.get_model()
        form_class = create_modelform(model)
        return form_class

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_success_url(self):
        return reverse_lazy('list_hardware', kwargs={'model': self.request.resolver_match.kwargs.get('model', None)})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_moderator'] = self.test_func()
        return context


class HardwareUpdateView(View, UserPassesTestMixin):
    template_name = 'hardware/edit_hardware.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Moderators').exists()

    def get(self, request, model, pk):
        model_class = get_model_from_model_name(self.kwargs.get('model'))

        ModelformClass = create_modelform(model_class)
        instance = get_object_or_404(model_class, pk=self.kwargs.get('pk'))
        form = ModelformClass(instance=instance)

        context = {
            'form': form,
            'model': model,
            'pk': pk,
            'user_is_moderator': self.test_func()
        }

        return render(request, self.template_name, context)

    def post(self, request, model, pk):
        model_class = get_model_from_model_name(self.request.resolver_match.kwargs.get('model'))

        ModelformClass = create_modelform(model_class)
        instance = get_object_or_404(model_class, pk=self.kwargs.get('pk'))
        form = ModelformClass(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('details_hardware', kwargs={'model': self.request.resolver_match.
                                                     kwargs.get('model'), 'pk': self.request.resolver_match.kwargs.get('pk')}))

        context = {
            'form': form,
            'model': model,
            'pk': pk,
            'user_is_moderator': self.test_func()
        }
        return render(request, self.template_name, context)


class HardwareDetailView(gen_views.DetailView, ValidateGroupMembershipMixin):
    template_name = 'hardware/details_hardware.html'
    context_object_name = 'component'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_object(self, queryset=None):
        model = self.get_model()
        if model is not None:
            pk = self.kwargs.get(self.pk_url_kwarg)
            return model.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_moderator'] = self.is_member_of_group('Moderators')
        context['excluded_fields'] = ['id', 'image']
        return context


class HardwareDeleteView(gen_views.DeleteView, UserPassesTestMixin):
    template_name = 'hardware/delete_hardware.html'
    context_object_name = 'component'

    def test_func(self):
        return self.request.user.groups.filter(name='Moderators').exists()

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_object(self, queryset=None):
        self.model = self.get_model()
        return super().get_object(queryset)

    def get_success_url(self):
        return reverse_lazy('list_hardware', kwargs={'model': self.request.resolver_match.kwargs.get('model', None)})

    def post(self, request, *args, **kwargs):
        storage = S3Boto3Storage()
        self.object = self.get_object()

        if self.object.image:
            storage.delete(self.object.image.name)
        success_url = self.get_success_url()
        self.object.delete()

        return redirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_moderator'] = self.test_func()
        return context

    def form_valid(self, form):
        storage = S3Boto3Storage()
        existing_instance = self.get_object()

        if 'image' in form.changed_data:

            image = existing_instance.image
            if image:
                storage.delete(image.name)

        return super().form_valid(form)


class HardwareListView(gen_views.ListView, ValidateGroupMembershipMixin):
    context_object_name = 'list'
    template_name = 'hardware/hardware_list.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_queryset(self):
        model = get_model_from_model_name(self.kwargs.get('model'))
        if model:
            return model.objects.all()
        else:
            raise ValueError("Invalid component selected.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_is_moderator'] = self.is_member_of_group('Moderators')
        return context