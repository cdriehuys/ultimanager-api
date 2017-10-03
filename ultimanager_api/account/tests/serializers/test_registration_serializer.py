from unittest import mock

from account import serializers


def test_create(db):
    """
    Saving a serializer with valid data should create a new user.
    """
    data = {
        'email': 'test@example.com',
        'password': 'password',
    }

    serializer = serializers.RegistrationSerializer(data=data)
    assert serializer.is_valid()

    user = serializer.save()

    assert user.email == data['email']
    assert user.check_password(data['password'])


def test_serialize(user_factory):
    """
    Test the serialized data produced by the serializer.
    """
    user = user_factory()
    serializer = serializers.RegistrationSerializer(user)

    expected = {
        'id': user.id,
        'email': user.email,
    }

    assert serializer.data == expected


def test_validate_password():
    """
    Validating the serializer should run the provided password through
    Django's password validation system.
    """
    password = 'password'
    serializer = serializers.RegistrationSerializer()

    with mock.patch(
            'account.serializers.password_validation.validate_password',
            autospec=True) as mock_validate:
        serializer.validate_password(password)

    assert mock_validate.call_count == 1
    assert set(mock_validate.call_args[0]) == {password}
