from django import forms

from TonysHardware_v2.common.models import ContactFormModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = '__all__'
