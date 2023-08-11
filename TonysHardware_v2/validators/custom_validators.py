from django.core.exceptions import ValidationError, PermissionDenied
import re

from django.shortcuts import redirect
from django.urls import reverse


def all_alpha_validator(value):
    if value.isalpha():
        return value
    else:
        raise ValidationError("Sorry, only letters (a-z) are allowed.")


def letters_numbers_and_underscores_validator(value):
    pattern = r'^[A-Za-z0-9_]*$'
    if not re.match(pattern, value):
        raise ValidationError("Sorry username can only consist of letters(a-z), numbers(0-9) and underscores(_).")
    else:
        return value


class ValidateAccountOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.pk == self.get_object().pk:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class ValidateGroupMembershipMixin:
    def is_member_of_group(self, group_name):
        user_groups = self.request.user.groups.all()
        return user_groups.filter(name=group_name).exists()
