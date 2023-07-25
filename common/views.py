from django.shortcuts import render
from django.views import generic as gen_views


class HomePageView(gen_views.TemplateView):
    template_name = 'common/index.html'