from django.urls import path, include
from rest_framework import routers

from .views import (
    GPTGetAPIView,
    GPTSendAPIView,
)

router = routers.SimpleRouter()
router.register("get_chatgpt", GPTGetAPIView)
router.register("send_chatgpt", GPTSendAPIView)


urlpatterns = [
    path("", include(router.urls)),
]
