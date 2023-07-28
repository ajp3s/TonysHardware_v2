from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.shortcuts import redirect
from django.urls import reverse
from storages.backends.s3boto3 import S3Boto3Storage

from TonysHardware_v2.accounts.forms import BasicUserRegisterForm, BasicUserEditProfileForm, BasicUserDeleteProfileForm, \
    UploadImageForm

BasicUserModel = get_user_model()


class ValidateAccountOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse('unauthorized'))


class UserCreationView(gen_views.CreateView):
    model = BasicUserModel
    form_class = BasicUserRegisterForm
    template_name = 'accounts/register.html'
    reverse_lazy('profile_details')

    def form_valid(self, form):
        submit = super().form_valid(form)
        login(self.request, self.object)
        return submit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next_url = self.request.GET.get('next', '')
        if next_url and '//' not in next_url:
            context['next'] = next_url
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next', '')
        if next_url:
            return next_url
        else:
            return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class UserEditProfileView(gen_views.UpdateView, LoginRequiredMixin, ValidateAccountOwnerMixin):
    model = BasicUserModel
    form_class = BasicUserEditProfileForm
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
    form_class = BasicUserDeleteProfileForm
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['message'] = 'Do you really want to delete your profile?\n This operation is irreversible.'
        context['form'] = BasicUserDeleteProfileForm(instance=obj, disabled=True)
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


class UploadImageView(gen_views.CreateView, LoginRequiredMixin, ValidateAccountOwnerMixin):
    template_name = 'accounts/upload_image.html'
    form_class = UploadImageForm
    success_url = reverse_lazy('profile_details')


class AccessDeniedView(gen_views.TemplateView):
    template_name = 'accounts/access_denied.html'
