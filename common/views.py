from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as gen_views

from TonysHardware_v2.common.forms import ContactForm
from TonysHardware_v2.common.models import ContactFormModel


class HomePageView(gen_views.TemplateView):
    template_name = 'common/index.html'


class ContactFormSubmissionView(gen_views.CreateView):
    model = ContactFormModel
    form_class = ContactForm
    template_name = 'common/contact_page.html'
    success_url = reverse_lazy('contact_form_success')


class ContactFormSubmissionSuccessView(gen_views.TemplateView):
    template_name = 'common/contact_form_submission_success.html'
