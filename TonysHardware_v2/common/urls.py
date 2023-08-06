from django.urls import include, path

from .views import HomePageView, ContactFormSubmissionView, ContactFormSubmissionSuccessView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),
    path('contact/', ContactFormSubmissionView.as_view(), name='contact_form'),
    path('contact/success', ContactFormSubmissionSuccessView.as_view(), name='contact_form_success'),
    path('about/', AboutPageView.as_view(), name='about')


]
