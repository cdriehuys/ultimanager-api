import pytest

import factories


@pytest.fixture
def user_factory(db):
    """
    Fixture to get the factory used to create users.

    Returns:
        The class used to create test ``User`` instances.
    """
    return factories.UserFactory
