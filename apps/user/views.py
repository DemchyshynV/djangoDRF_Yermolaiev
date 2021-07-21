from rest_framework.generics import ListCreateAPIView

from .serializers import UserSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
