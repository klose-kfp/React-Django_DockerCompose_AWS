from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView


class UserList(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
