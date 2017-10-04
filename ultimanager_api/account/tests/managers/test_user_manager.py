from account import models


def test_create_superuser(db):
    """
    Creating a superuser should do the same thing as a normal user
    except ``is_staff`` and ``is_superuser`` should be set to true.
    """
    email = 'test@example.com'
    password = 'password'

    user = models.User.objects.create_superuser(email, password)

    assert user.email == email
    assert user.is_staff
    assert user.is_superuser


def test_create_user(db):
    """
    Passing an email and password to the method should create a new user
    with the given attributes.
    """
    email = 'test@example.com'
    password = 'password'

    user = models.User.objects.create_user(email, password)

    assert user.email == email
    assert user.check_password(password)
