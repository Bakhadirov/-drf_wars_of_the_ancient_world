import pytest
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient
from main_app.apps.users.models import User


@pytest.mark.django_db
def test_profile_401_unauthorized(api_client: APIClient):
    response = api_client.get('/api/v1/users/profile/')

    assert response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_profile_200(authorized_api_client: APIClient, user: User):

    response = authorized_api_client.get('/api/v1/users/profile/')

    assert response.status_code == HTTP_200_OK
    assert response.json() == {
        'id': user.id,
        'avatar': None,
        'birthday': str(user.birthday),
        'contact_telephone': str(user.contact_telephone),
        'email': user.email,
        'extra_information': user.extra_information,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'patronymic': user.patronymic,
        'username': 'username',
    }
