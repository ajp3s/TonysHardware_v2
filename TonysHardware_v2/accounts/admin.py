from django.contrib import admin

from TonysHardware_v2.accounts.models import BasicUser, UserImageGalleryModel


@admin.register(BasicUser)
class BasicUserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    list_filter = ('date_joined', 'groups')
    list_per_page = 10


@admin.register(UserImageGalleryModel)
class UserImageGalleryModelAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'image')
    list_filter = ('user_profile',)


