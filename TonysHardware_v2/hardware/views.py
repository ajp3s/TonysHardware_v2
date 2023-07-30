from django.urls import reverse_lazy
from django.views import generic as gen_views


from .utils import create_hardware_model_form, get_model_from_model_name


class HardwareAddView(gen_views.CreateView):
    template_name = 'hardware/add_hardware.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.request, **self.get_form_kwargs())

    def get_success_url(self):
        return reverse_lazy('details_hardware', kwargs={'model': self.get_model(), 'pk': self.object.pk})


class HardwareUpdateView(gen_views.UpdateView):

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.request, **self.get_form_kwargs())

    def get_object(self, queryset=None):
        model = self.get_model()
        if model is not None:
            pk = self.kwargs.get(self.pk_url_kwarg)
            return model.objects.get(pk=pk)

    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return reverse_lazy('details_hardware', kwargs={'model': self.get_model(), 'pk': self.object.pk})


class HardwareDetailView(gen_views.DetailView):
    template_name = 'hardware/details_hardware.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_object(self, queryset=None):
        model = self.get_model()
        if model is not None:
            pk = self.kwargs.get(self.pk_url_kwarg)
            return model.objects.get(pk=pk)


class HardwareDeleteView(gen_views.DeleteView):
    template_name = 'hardware/delete_hardware.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_object(self, queryset=None):
        self.model = self.get_model()
        return super().get_object(queryset)

    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return reverse_lazy('list_hardware', kwargs={'model': self.get_model(), 'pk': pk})

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.request, **self.get_form_kwargs())


class HardwareListView(gen_views.ListView):
    context_object_name = 'list'
    template_name = 'hardware/hardware_list.html'
    print(context_object_name)

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_queryset(self):
        model = self.get_model()
        if model:
            return model.objects.all()
        else:
            raise ValueError("Invalid model specified.")