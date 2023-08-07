from django.shortcuts import redirect
from django.urls import reverse


class ValidateAccountOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse('unauthorized'))
