from django.contrib.auth.models import AbstractUser
from TonysHardware_v2.validators.custom_validators import letters_numbers_and_underscores_validator
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class BasicUser(AbstractUser):
    username = models.CharField(
        unique=True,
        max_length=50,
        validators=(
            letters_numbers_and_underscores_validator,
        ),
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default="",

    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default="",

    )
    email = models.EmailField(
        unique=True,
    )

    additional_information = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        default="",

    )

    profile_picture = models.FileField(
        upload_to='media/profile_pictures/',
        null=True,
        blank=True,

    )

    def full_name(self):
        full_name = f'{self.first_name} {self.last_name}' if self.first_name or self.last_name else ""
        return full_name

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()

        if self.profile_picture:
            self.profile_picture.name = self.profile_picture.name
            self.profile_picture = storage.save(self.profile_picture.name, self.profile_picture)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name()


class ImageGalleryModel(models.Model):
    user_profile = models.ForeignKey(
        BasicUser,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        upload_to='gallery_images/',

    )

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()

        if self.image:
            self.image.name = self.image.name
            self.image = storage.save(self.image.name, self.image)

            super().save(*args, **kwargs)
