from django.contrib.auth.forms import UserCreationForm

from TonysHardware_v2.accounts.models import BasicUser


class BasicUserBaseForm(UserCreationForm):
    class Meta:
        model = BasicUser
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'profile_picture',
        ]


class BasicUserCreationForm(BasicUserBaseForm):
    pass


class BasicUserEditForm(BasicUserBaseForm):
    pass


class BasicUserDeleteForm(BasicUserBaseForm):
    pass
