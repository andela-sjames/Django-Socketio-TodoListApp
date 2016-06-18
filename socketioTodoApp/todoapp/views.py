
# from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.decorators.http import require_http_methods
from todoapp.models import Todo
# from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):

    template_name = 'index.html'


@require_http_methods(["GET", "POST"])
def my_todo(request):
    if request.method == 'POST':
        name = request.POST.get('todo_name', '')
        todo = Todo(name=name)
        todo.save()
