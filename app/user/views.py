"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions # noqa
from rest_framework.authtoken.views import ObtainAuthToken # noqa
from rest_framework.settings import api_settings # noqa

from user.serializers import (
    UserSerializer,

)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
