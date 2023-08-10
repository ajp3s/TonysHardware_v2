from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import models

from TonysHardware_v2.accounts.models import UserImageGalleryModel

BasicUserModel = get_user_model()


class BasicUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BasicUserRegisterForm, self).__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

    class Meta:
        model = BasicUserModel
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'profile_picture',
        ]


class BasicUserEditProfileForm(forms.ModelForm):

    class Meta:
        model = BasicUserModel
        fields = [
            'username',
            'first_name',
            'last_name',
            'profile_picture',
            'additional_information',

        ]


class BasicUserDeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        disabled = kwargs.pop('disabled', False)
        super(BasicUserDeleteProfileForm, self).__init__(*args, **kwargs)

        if disabled:
            for field in self.fields.values():
                field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = BasicUserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserImageGalleryModel
        fields = [
            'image',
        ]
