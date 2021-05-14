from django.urls import path
from .consumers import Consumer

ws_urlpatterns = [
    path('ws/', Consumer.as_asgi()),
]