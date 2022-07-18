import pytest
from rest_framework.test import APIClient
from typing import Any, Dict
#
# from main_app.apps.users.models import User
from main_app.apps.users.models import User
from tests.factory.users import UserFactory
#

@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()
#
@pytest.fixture()
def user() -> User:
    return UserFactory(username='username', password='password')

@pytest.fixture()
def authorized_api_client(api_client: APIClient, user: User) -> APIClient:
    api_client.force_authenticate(user)
    return api_client

#
@pytest.fixture()
def user_update_data(user: User) -> Dict[str, Any]:
    return {
        'first_name': UserFactory().first_name,
        'last_name': UserFactory().last_name,
        'patronymic': UserFactory().patronymic,
        'avatar': None,
        'contact_telephone': '+79161233212',
        'extra_information': '',
    }


@pytest.fixture()
def user_registration_data() -> Dict[str, Any]:
    return {
        'username': 'username',
        'email': 'username@gmail.com',
        'password1': 'password',
        'password2': 'password',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'birthday': '1990-01-01',
        'patronymic': 'patronymic',
        'contact_telephone': '+77777777777',
        'extra_information': 'extra_information'
    }