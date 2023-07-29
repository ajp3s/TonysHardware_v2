from django.core.exceptions import ValidationError
import re


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
