from django.contrib import admin

from TonysHardware_v2.common.models import ContactFormModel, ArticleModel


@admin.register(ContactFormModel)
class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_at', 'email', 'message']
    list_filter = ['subject']
    sortable_by = ['created_at']


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'added_at', 'source']
    list_filter = ['source']
    sortable_by = ['added_at']