from django import forms

from TonysHardware_v2.common.models import ContactFormModel, ArticleModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = '__all__'


class ArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = '__all__'
