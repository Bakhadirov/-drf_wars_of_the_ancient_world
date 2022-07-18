


from typing import Any, Dict

import pytest
from django.forms import model_to_dict
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK,
)
from rest_framework.test import APIClient

from main_app.apps.users.models import User


@pytest.mark.django_db
def test_update_401_unauthorized_user(
    api_client: APIClient,
    user: User,
    user_update_data: Dict[str, Any],
):

    response = api_client.patch(
        f'/api/v1/users/profile/', data=user_update_data,)

    assert response.status_code == HTTP_401_UNAUTHORIZED



@pytest.mark.django_db
def test_update_200_user(
    authorized_api_client: APIClient,
    user_update_data: Dict[str, Any],
    user: User

):

    response = authorized_api_client.patch('/api/v1/users/profile/', data=user_update_data,)

    user.refresh_from_db()
    assert response.status_code == HTTP_200_OK
    assert response.json() == {'user':{
        'id': user.id,
        'avatar': None,
        'birthday': str(user.birthday),
        'contact_telephone': '+79161233212',
        'email': user.email,
        'extra_information': '',
        'first_name': user.first_name,
        'last_name': user.last_name,
        'patronymic': user.patronymic,
        'username': 'username',
    }}