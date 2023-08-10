from django.urls import include, path

from .views import ContactFormSubmissionView, ContactFormSubmissionSuccessView, AboutPageView, \
    ArticleAddView, ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='home page'),
    path('addarticle/', ArticleAddView.as_view(), name='add_article'),
    path('contact/', ContactFormSubmissionView.as_view(), name='contact_form'),
    path('contact/success', ContactFormSubmissionSuccessView.as_view(), name='contact_form_success'),
    path('about/', AboutPageView.as_view(), name='about')

]
