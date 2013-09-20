from django.contrib.auth.models import User
from rest_framework import viewsets

from users import serializers


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = serializers.UserSerializer
