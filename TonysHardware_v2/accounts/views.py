from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.shortcuts import redirect
from storages.backends.s3boto3 import S3Boto3Storage


from TonysHardware_v2.accounts.forms import BasicUserRegisterForm, BasicUserEditProfileForm, BasicUserDeleteProfileForm, \
    UploadImageForm
from TonysHardware_v2.validators.custom_validators import ValidateAccountOwnerMixin
from TonysHardware_v2.accounts.models import GalleryImage

BasicUserModel = get_user_model()


class UserCreateProfileView(gen_views.CreateView):
    model = BasicUserModel
    form_class = BasicUserRegisterForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        submit = super().form_valid(form)
        form.save(submit)
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


class UserEditProfileView(LoginRequiredMixin, ValidateAccountOwnerMixin, gen_views.UpdateView):
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

    def form_valid(self, form):
        storage = S3Boto3Storage()
        existing_instance = self.get_object()

        if 'profile_picture' in form.changed_data:

            old_picture = existing_instance.profile_picture

            if old_picture:
                storage.delete(old_picture.name)

        return super().form_valid(form)


class UserDeleteProfileView(LoginRequiredMixin, ValidateAccountOwnerMixin, gen_views.DeleteView):
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
        success_url = self.get_success_url()

        if self.object.profile_picture:
            storage.delete(self.object.profile_picture.name)

        self.object.delete()

        return redirect(success_url)


class UserProfileDetailsView(LoginRequiredMixin, gen_views.DetailView):
    model = BasicUserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery = GalleryImage.objects.filter(user_id=self.object.pk)

        context['gallery'] = gallery
        context['is_owner'] = (
                self.request.user.is_authenticated and
                self.request.user.username == self.get_object().username
        )

        return context


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


class UploadImageView(LoginRequiredMixin, gen_views.CreateView):
    model = GalleryImage
    form_class = UploadImageForm
    template_name = 'accounts/upload_image.html'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy('profile_details', kwargs={'pk': self.request.user.pk})


class UsersListView(LoginRequiredMixin, gen_views.ListView):
    template_name = 'accounts/users_list.html'
    model = BasicUserModel
    context_object_name = 'users_list'
