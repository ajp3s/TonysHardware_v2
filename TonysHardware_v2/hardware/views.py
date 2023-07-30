from django.views import generic as gen_views
from .utils import get_model_from_query_params, create_hardware_model_form


class HardwareAddView(gen_views.CreateView):
    model = None

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.request, **self.get_form_kwargs())

    def get_model(self, model_name):
        model = get_model_from_query_params(self.request)
        return model

    def get_success_url(self):
        return '/success/'


class HardwareUpdateView(gen_views.UpdateView):
    model = None

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.request, **self.get_form_kwargs())

    def get_object(self, queryset=None):
        self.model = get_model_from_query_params(self.request)
        return super().get_object(queryset)

    def get_success_url(self):
        return '/success/'


class HardwareDetailView(gen_views.DetailView):
    model = None

    def get_object(self, queryset=None):
        self.model = get_model_from_query_params(self.request)
        return super().get_object(queryset)


class HardwareDeleteView(gen_views.DeleteView):
    model = None

    def get_object(self, queryset=None):
        self.model = get_model_from_query_params(self.request)
        return super().get_object(queryset)

    def get_success_url(self):
        return '/success/'

    def get_form(self, form_class=None):
        return create_hardware_model_form(self.request, **self.get_form_kwargs())


class HardwareListView(gen_views.ListView):
    model = None

    def get_queryset(self):
        self.model = get_model_from_query_params(self.request)
        return super().get_queryset()
