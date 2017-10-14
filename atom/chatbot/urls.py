from django.conf.urls import url
from . import views

app_name = 'chatbot'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chatbot_help/$', views.chatbot_help, name='chatbot_help'),
    url(r'^developers/$', views.developers, name='developers'),
]
