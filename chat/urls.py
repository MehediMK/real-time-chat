from django.urls import path
from chat.views import index


urlpatterns = [
    path('chat/', index, name='chat')
]