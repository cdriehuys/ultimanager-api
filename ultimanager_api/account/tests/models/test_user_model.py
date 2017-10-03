from account import models


def test_create_user(db):
    """
    Test creating a new user.
    """
    user = models.User(email='test@example.com')
    user.save()

    # Test defaults.
    assert not user.email_verified
    assert not user.is_staff


def test_get_full_name(user_factory):
    """
    The user's full name should be their email address.
    """
    user = user_factory()

    assert user.get_full_name() == user.email


def test_get_short_name(user_factory):
    """
    The user's short name should be their email address.
    """
    user = user_factory()

    assert user.get_short_name() == user.email
