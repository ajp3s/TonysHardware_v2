from django.contrib.auth.models import AbstractUser
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

from TonysHardware_v2.settings import AWS_S3_CUSTOM_DOMAIN


class BasicUser(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=50
    )

    first_name = models.CharField(
        max_length=30,

    )

    last_name = models.CharField(
        max_length=30,

    )
    email = models.EmailField(
        unique=True,
    )

    additional_information = models.TextField(
        max_length=300,

    )

    profile_picture = models.FileField(
        upload_to='profile_pictures/',
        null=True,
        blank=True,

    )

    def save(self, *args, **kwargs):
        if self.profile_picture:
            storage = S3Boto3Storage()
            self.profile_picture.name = self.profile_picture.name
            self.profile_picture = storage.save(self.profile_picture.name, self.profile_picture)

        super().save(*args, **kwargs)
