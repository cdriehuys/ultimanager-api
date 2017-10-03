"""
Models to store account related functionality.
"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from account import managers


class User(PermissionsMixin, AbstractBaseUser):
    """
    Model to store a user's account information.
    """
    email = models.EmailField(
        unique=True,
        verbose_name=_('email'))
    email_verified = models.BooleanField(
        default=False,
        verbose_name=_('email verified'))
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Staff users are allow to log in to the admin panel.'),
        verbose_name=_('is staff'))

    # Constants for Django
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    # Custom manager
    objects = managers.UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Get the user's full name.

        Returns:
            The user's email address.
        """
        return self.email

    def get_short_name(self):
        """
        Get the user's short name.

        Returns:
            The user's email address.
        """
        return self.email
