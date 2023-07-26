from django.contrib.auth.models import User
from django.urls import path

from TonysHardware_v2.accounts.views import UserCreationView, UserProfileDetailsView, UserLoginView, \
    UserLogoutView, UserDeleteProfileView

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='register'),
    path('details/<int:pk>', UserProfileDetailsView.as_view(), name='profile_details'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/<int:pk>', UserLogoutView.as_view(), name='logout'),
    path('delete/<int:pk>', UserDeleteProfileView.as_view(), name='delete_profile'),
]
