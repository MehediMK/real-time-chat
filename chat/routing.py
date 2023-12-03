# from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import ChatConsumer


ws_urlpatterns = [
    path('ws/chat/', ChatConsumer.as_asgi())
]