from django.urls import re_path
from . import consumer


websocket_urlpatterns = [
     re_path(r"ws/chat/(?P<product_id>\d+)/$", consumer.ChatConsumer.as_asgi())
]