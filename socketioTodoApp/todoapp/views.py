
# from django.shortcuts import render

from django.views.generic.base import TemplateView
# from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):

    template_name = 'todoapp/index.html'
