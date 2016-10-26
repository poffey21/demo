from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MessageView.as_view(), name='chat-session'),
]