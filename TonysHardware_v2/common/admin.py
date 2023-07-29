from django.contrib import admin

from TonysHardware_v2.common.models import ContactFormModel


@admin.register(ContactFormModel)
class ContactFormModelAdmin(admin.ModelAdmin):
    pass

