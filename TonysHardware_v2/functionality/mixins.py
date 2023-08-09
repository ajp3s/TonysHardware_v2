from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class S3ImageSaveMixin(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        storage = S3Boto3Storage()

        if self.image:
            self.image.name = self.image.name
            self.image = storage.save(self.image.name, self.image)

        super().save(*args, **kwargs)
