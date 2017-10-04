"""
Managers for account related models.
"""

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager for the ``User`` model.
    """

    def create_superuser(self, email, password, **kwargs):
        """
        Create a user with all permissions.

        Args:
            email:
                The user's email address.
            password:
                The user's password.
            kwargs:
                Any additional arguments to pass to the user.

        Returns:
            The newly created user instance.
        """
        user = self.create_user(
            email=email,
            is_staff=True,
            is_superuser=True,
            password=password,
            **kwargs)

        return user

    def create_user(self, email, password=None, **kwargs):
        """
        Create a new ``User`` instance.

        Args:
            email:
                The user's email address.
            password:
                The user's password.
            kwargs:
                Any additional arguments to pass to the user.

        Returns:
            The newly created user instance.
        """
        user = self.model(email=email, **kwargs)
        user.set_password(password)

        user.save()

        return user
