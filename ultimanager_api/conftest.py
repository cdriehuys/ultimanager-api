import pytest

import factories

from rest_framework.test import APIRequestFactory


@pytest.fixture
def api_rf():
    """
    Fixture to get a factory used to make API requests.

    Returns:
        An instance of the request factory provided by DRF.
    """
    return APIRequestFactory()


@pytest.fixture
def user_factory(db):
    """
    Fixture to get the factory used to create users.

    Returns:
        The class used to create test ``User`` instances.
    """
    return factories.UserFactory
