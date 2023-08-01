from django.urls import reverse_lazy
from django.views import generic as gen_views


from .utils import create_hardware_model_form, get_model_from_model_name


class HardwareAddView(gen_views.CreateView):
    template_name = 'hardware/add_hardware.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.get_model())

    def get_success_url(self):
        return reverse_lazy('details_hardware', kwargs={'model': self.get_model(), 'pk': self.object.pk})

    def form_valid(self, form):
        print("Form is valid:", form.is_valid())

        if form.is_valid():
            self.object = form.save()
            print("Form data saved successfully.")
            return super().form_valid(form)

        print("Form data not saved. Form errors:", form.errors)
        return self.form_invalid(form)


class HardwareUpdateView(gen_views.UpdateView):
    template_name = 'hardware/edit_hardware.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.get_model())

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

    def form_valid(self, form):
        instance = self.get_object()
        instance.delete()
        return super().form_valid(form)


class HardwareListView(gen_views.ListView):
    context_object_name = 'list'
    template_name = 'hardware/hardware_list.html'

    def get_model(self):
        return get_model_from_model_name(self.kwargs.get('model'))

    def get_queryset(self):
        model = self.get_model()
        if model:
            return model.objects.all()
        else:
            raise ValueError("Invalid component selected.")
