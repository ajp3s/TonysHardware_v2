from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic as gen_views

from TonysHardware_v2.common.forms import ContactForm
from TonysHardware_v2.common.models import ContactFormModel, ArticleModel
from TonysHardware_v2.functionality.funcs import create_modelform


class ArticleListView(gen_views.ListView):
    model = ArticleModel
    context_object_name = 'articles'
    template_name = 'common/index.html'
    ordering = ['added_at']


class ArticleDetailView(gen_views.DetailView):
    model = ArticleModel


class ContactFormSubmissionView(gen_views.CreateView):
    model = ContactFormModel
    form_class = ContactForm
    template_name = 'common/contact_page.html'
    success_url = reverse_lazy('contact_form_success')


class ContactFormSubmissionSuccessView(gen_views.TemplateView):
    template_name = 'common/contact_form_submission_success.html'


class AboutPageView(gen_views.TemplateView):
    template_name = 'common/about.html'


class ArticleAddView(LoginRequiredMixin, UserPassesTestMixin, gen_views.CreateView):
    model = ArticleModel
    form_class = create_modelform(model)
    template_name = 'common/article_create.html'
    success_url = reverse_lazy('home page')

    def test_func(self):
        return self.request.user.groups.filter(name='Writers').exists()




