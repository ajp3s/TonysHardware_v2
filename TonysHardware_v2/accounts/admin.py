from django.contrib import admin

from TonysHardware_v2.accounts.models import BasicUser, GalleryImage


@admin.register(BasicUser)
class BasicUserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    list_filter = ('date_joined', 'groups')
    list_per_page = 10


@admin.register(GalleryImage)
class UserImageGalleryModelAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
    list_filter = ('user_id',)


