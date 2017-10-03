from rest_framework import status
from rest_framework.reverse import reverse

from account import models, serializers, views


registration_view = views.RegistrationView.as_view()
url = reverse('account:register')


def test_post_registration_info(api_rf, db):
    """
    Sending a POST request with valid data to the view should create a
    new user.
    """
    data = {
        'email': 'test@example.com',
        'password': 'password',
    }

    request = api_rf.post('/', data)
    response = registration_view(request)

    assert response.status_code == status.HTTP_201_CREATED

    serializer = serializers.RegistrationSerializer(models.User.objects.get())

    assert response.data == serializer.data
