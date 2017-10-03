"""
Serializers for account related information.
"""

from django.contrib.auth import get_user_model, password_validation

from rest_framework import serializers


UserModel = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """

    class Meta:
        extra_kwargs = {
            'password': {
                'style': {'input_type': 'password'},
                'write_only': True,
            },
        }
        fields = ('id', UserModel.EMAIL_FIELD, 'password')
        model = UserModel

    def create(self, data):
        """
        Register a new user.

        Args:
            data:
                The data to create a new user from.

        Returns:
            The newly created user.
        """
        return UserModel.objects.create_user(**data)

    def validate_password(self, password):
        """
        Validate the provided password.

        Args:
            password:
                The password to validate.

        Returns:
            The validated password.
        """
        password_validation.validate_password(password)

        return password
