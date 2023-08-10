from django.contrib import admin

from TonysHardware_v2.common.models import ContactFormModel, ArticleModel


@admin.register(ContactFormModel)
class ContactFormModelAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    pass
