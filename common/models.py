from django.core.validators import MinLengthValidator
from django.db import models


class ContactFormModel(models.Model):
    username = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    subject = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    message = models.TextField(
        max_length=500,
        validators=(
            MinLengthValidator(10),
        ),
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
