from rest_framework import serializers
from .models import (
    GPTModel,
)


class GPTSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTModel
        fields = (
            "loginuser",
            "author",
            "Title",
            "Mermaid",
            "svg",
            "text",
            "UpdatedDate",
        )
