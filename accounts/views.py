import boto3
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as gen_views

from TonysHardware_v2.accounts.forms import BasicUserCreationForm
from TonysHardware_v2.settings import AWS_STORAGE_BUCKET_NAME

BasicUserModel = get_user_model()


class UserCreationView(gen_views.CreateView):
    model = BasicUserModel
    form_class = BasicUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('profile_details')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


class UsersListView(gen_views.ListView):
    model = BasicUserModel


class UserProfileDetailsView(gen_views.DetailView):
    model = BasicUserModel
    template_name = 'accounts/profile_details.html'
    context_object_name = 'user'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('profile_details', kwargs={'pk': pk})


class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home page')
