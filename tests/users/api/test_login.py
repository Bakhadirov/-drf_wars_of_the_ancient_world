import pytest
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APIClient
from main_app.apps.users.models import User


@pytest.mark.django_db
def test_login_200(api_client: APIClient, user: User):
    response = api_client.post(
        '/api/v1/users/login/',
        data={
            'username': 'username',
            'password': 'password',
        },
    )

    assert response.status_code == HTTP_200_OK
    assert response.json()['token'] == Token.objects.get(user=user).key


@pytest.mark.django_db
def test_login_400(api_client: APIClient, user: User):
    response = api_client.post('/api/v1/users/login/', data={'username': '', 'password': ''})

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert Token.objects.count() == 0
