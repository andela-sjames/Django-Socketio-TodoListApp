
# from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from todoapp.models import Todo
# from django_socketio import broadcast_channel
from django_socketio import events
from django.utils.html import strip_tags
# from django.core.urlresolvers import reverse_lazy


class HomeView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return self.render_to_response(context)

# Ajax implemented here first before using socktio below.
@require_http_methods(["GET", "POST"])
def my_todo(request):
    if request.method == 'POST':
        name = request.POST.get('todo_name', '')
        todo = Todo(name=name)
        todo.save()

        return HttpResponse("success", content_type="text/plain")


@events.on_message(channel="added")
def message(request, socket, context, message):
    if message["action"] == "add":
        name = strip_tags(message["message"])
        print name + ' ==this is the name== ' + name
        todo = Todo(name=name)
        todo.save()
        done = {"action": "done", "name": name}

        socket.send_and_broadcast_channel(done)
    else:
        done = {"action": "no", "name": 'waiting'}
        socket.send_and_broadcast_channel(done)
