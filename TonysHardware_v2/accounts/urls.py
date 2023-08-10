from django.contrib.auth.models import User
from django.urls import path

from TonysHardware_v2.accounts.views import UserCreateProfileView, UserProfileDetailsView, UserLoginView, \
    UserLogoutView, UserDeleteProfileView, UserEditProfileView, UploadImageView, AccessDeniedView

urlpatterns = [
    path('register/', UserCreateProfileView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('details/<int:pk>', UserProfileDetailsView.as_view(), name='profile_details'),
    path('logout/<int:pk>', UserLogoutView.as_view(), name='logout'),
    path('delete/<int:pk>', UserDeleteProfileView.as_view(), name='delete_profile'),
    path('edit/<int:pk>', UserEditProfileView.as_view(), name='edit_profile'),
    path('details/<int:pk>/upload_image', UploadImageView.as_view(), name='upload_image'),
    path('access-denied/', AccessDeniedView.as_view(), name='access_denied'),

]
