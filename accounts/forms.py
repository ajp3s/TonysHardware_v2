from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

BasicUserModel = get_user_model()


class BasicUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BasicUserCreationForm, self).__init__(*args, **kwargs)

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


class BasicUserEditForm(forms.ModelForm):
    class Meta:
        model = BasicUserModel
        fields = [
            'username',
            'first_name',
            'last_name',
            'profile_picture',
            'additional_information',

        ]

        def save(self, commit=True):
            save = self.model.save()


class BasicUserDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        disabled = kwargs.pop('disabled', False)
        super(BasicUserDeleteForm, self).__init__(*args, **kwargs)

        if disabled:
            for field in self.fields.values():
                field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = BasicUserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']
