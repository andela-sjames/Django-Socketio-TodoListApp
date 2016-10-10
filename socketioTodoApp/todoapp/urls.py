from django.conf.urls import url
from todoapp import views


urlpatterns = [

    url(r'^listen/$', views.my_todo, name='mytodo')
]
