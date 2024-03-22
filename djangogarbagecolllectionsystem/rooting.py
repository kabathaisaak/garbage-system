# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from yourapp import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/speech-to-sign-language/", consumers.SignLanguageConsumer.as_asgi()),
    ]),
})
