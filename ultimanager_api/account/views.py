"""
Views for accessing and modifying account information.
"""

from rest_framework import generics

from account import serializers


class RegistrationView(generics.CreateAPIView):
    """
    View for registering a new user.
    """
    serializer_class = serializers.RegistrationSerializer
