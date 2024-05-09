from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('server/', consumers.ServerConsumer.as_asgi()),
]