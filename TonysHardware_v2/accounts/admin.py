from django.contrib import admin

from TonysHardware_v2.accounts.models import BasicUser, UserImageGalleryModel


@admin.register(BasicUser)
class BasicUserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "full_name", 'email')


@admin.register(UserImageGalleryModel)
class UserImageGalleryModelAdmin(admin.ModelAdmin):
    pass
