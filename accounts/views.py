from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.shortcuts import redirect
from django.urls import reverse
from storages.backends.s3boto3 import S3Boto3Storage

from TonysHardware_v2.accounts.forms import BasicUserCreationForm, BasicUserEditForm, BasicUserDeleteForm

BasicUserModel = get_user_model()


class ValidateAccountOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse('unauthorized'))


class UserCreationView(gen_views.CreateView):
    model = BasicUserModel
    form_class = BasicUserCreationForm
    template_name = 'accounts/register.html'
    reverse_lazy('profile_details')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next = self.request.POST.get('next', '')
        context['pk'] = self.request.user.pk

        if next != "?":
            context['next'] = next

        return context

    def get_success_url(self):
        success_url = self.request.POST.get('next', self.success_url(kwargs={'pk': self.request.user.pk}))
        return success_url


class UserEditProfileView(gen_views.UpdateView, LoginRequiredMixin, ValidateAccountOwnerMixin):
    model = BasicUserModel
    form_class = BasicUserEditForm
    template_name = 'accounts/edit_profile.html'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('profile_details', kwargs={'pk': pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs


class UserDeleteProfileView(gen_views.DeleteView, LoginRequiredMixin, ValidateAccountOwnerMixin):
    model = BasicUserModel
    form_class = BasicUserDeleteForm
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['message'] = 'Do you really want to delete your profile?\n This operation is irreversible.'
        context['form'] = BasicUserDeleteForm(instance=obj, disabled=True)
        return context

    def post(self, request, *args, **kwargs):
        storage = S3Boto3Storage()
        self.object = self.get_object()
        if self.object.profile_picture:
            storage.delete(self.object.profile_picture.name)
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)


class UserProfileDetailsView(gen_views.DetailView, LoginRequiredMixin):
    model = BasicUserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        print(result.get('user').date_joined)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.POST.get('next', '')
        return context

    def get_success_url(self):
        pk = self.request.user.pk
        return self.request.POST.get('next', reverse_lazy('profile_details', kwargs={'pk': pk}))


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home page')


class AccessDeniedView(gen_views.TemplateView):
    template_name = 'accounts/access_denied.html'
