from .models import (
    GPTModel,
)
from rest_framework import viewsets
from .serializers import (
    GPTSerializer,
)


class GPTGetAPIView(viewsets.ModelViewSet):
    queryset = GPTModel.objects.all().order_by("-UpdatedDate")
    serializer_class = GPTSerializer


class GPTSendAPIView(viewsets.ModelViewSet):
    queryset = GPTModel.objects.all()
    serializer_class = GPTSerializer
