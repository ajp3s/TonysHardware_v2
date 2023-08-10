from django.urls import reverse_lazy
from django.views import generic as gen_views

from TonysHardware_v2.common.forms import ContactForm
from TonysHardware_v2.common.models import ContactFormModel, ArticleModel
from TonysHardware_v2.functionality.funcs import create_modelform


class HomePageView(gen_views.TemplateView):
    template_name = 'common/index.html'


class ContactFormSubmissionView(gen_views.CreateView):
    model = ContactFormModel
    form_class = ContactForm
    template_name = 'common/contact_page.html'
    success_url = reverse_lazy('contact_form_success')


class ContactFormSubmissionSuccessView(gen_views.TemplateView):
    template_name = 'common/contact_form_submission_success.html'


class AboutPageView(gen_views.TemplateView):
    template_name = 'common/about.html'


class ArticleCreateView(gen_views.CreateView):
    model = ArticleModel
    form_class = create_modelform(model)
    template_name = 'common/article_create.html'
    success_url = reverse_lazy('home page')


class ArticleListView(gen_views.ListView):
    model = ArticleModel
    context_object_name = 'articles'
    template_name = 'common/index.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('added_at')

