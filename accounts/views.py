from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as gen_views
from django.shortcuts import redirect
from django.urls import reverse
from TonysHardware_v2.accounts.forms import BasicUserCreationForm, BasicUserEditForm, BasicUserDeleteForm

BasicUserModel = get_user_model()


class ValidateUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse('unauthorized'))


class UserCreationView(gen_views.CreateView):
    model = BasicUserModel
    form_class = BasicUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('profile_details')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class UserEditProfileView(gen_views.UpdateView):
    model = BasicUserModel
    form_class = BasicUserEditForm
    template_name = 'accounts/edit_profile.html'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('profile_details', kwargs={'pk': pk})


class UserDeleteProfileView(gen_views.DeleteView):
    model = BasicUserModel
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('home page')
    form_class = BasicUserDeleteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['message'] = 'Do you really want to delete your profile?\n This operation is irreversible.'
        context['form'] = BasicUserDeleteForm(instance=obj, disabled=True)
        return context


class UserProfileDetailsView(gen_views.DetailView):
    model = BasicUserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        print(result.get('user').date_joined)


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('profile_details', kwargs={'pk': pk})


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home page')


class AccessDeniedView(gen_views.TemplateView):
    template_name = 'accounts'