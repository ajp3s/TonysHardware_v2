from django.contrib.auth.models import Group
from django.core.validators import MinLengthValidator
from django.db import models

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from TonysHardware_v2.functionality.mixins import S3ImageSaveMixin


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


class ArticleModel(S3ImageSaveMixin, models.Model):
    title = models.CharField(
        max_length=70,
        null=False,
        blank=False,
    )

    image = models.ImageField(
        upload_to='article_images/',

    )

    content = models.TextField(
        max_length=500,
        null=False,
        blank=False,

    )

    added_at = models.DateTimeField(
        auto_now_add=True,
    )

    source = models.CharField(
        max_length=50,

    )

    def __str__(self):
        return f'{self.title}'
