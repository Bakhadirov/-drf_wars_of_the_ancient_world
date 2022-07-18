import datetime
from typing import Any, Dict
import pytest
from django.forms import model_to_dict
from phonenumbers import PhoneNumber
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.test import APIClient
from main_app.apps.users.models import User


@pytest.mark.django_db
def test_registration_200_project(
    api_client: APIClient,
    user_registration_data: Dict[str, Any],
):

    response = api_client.post('/api/v1/users/registration/', data=user_registration_data)
    user = User.objects.get()
    assert response.status_code == HTTP_201_CREATED
    assert model_to_dict(
        user,
        exclude=(
            'password1',
            'password2',
            'avatar',
            'date_joined',
            'is_staff',
            'password',
            'user_permissions',
            'last_login',
        ),
    ) == {
        'id': user.id,
        'username': user_registration_data['username'],
        'email': user_registration_data['email'],
        'first_name': user_registration_data['first_name'],
        'last_name': user_registration_data['last_name'],
        'patronymic': user_registration_data['patronymic'],
        'birthday': datetime.date(1990, 1, 1),
        'contact_telephone': PhoneNumber(country_code=7, national_number=7777777777, country_code_source=1),
        'is_active': True,
        'is_superuser': False,
        'groups': [],
        'extra_information': 'extra_information',
    }

    assert response.json() == {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'patronymic': user.patronymic,
        'birthday': '1990-01-01',
        'contact_telephone': '+77777777777',
        'avatar': None,
        'extra_information': 'extra_information',
    }


@pytest.mark.django_db
def test_registration_400_password_differ(
    api_client: APIClient,
    user_registration_data: Dict[str, Any],
):
    user_registration_data['password1'] = 'password1'
    user_registration_data['password2'] = 'password2'

    response = api_client.post('/api/v1/users/registration/', data=user_registration_data)

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {'non_field_errors': ["Passwords don't match"]}


@pytest.mark.django_db
def test_registration_400_incorrect_phone_number(
    api_client: APIClient,
    user_registration_data: Dict[str, Any],
):
    user_registration_data['contact_telephone'] = '+7'

    response = api_client.post('/api/v1/users/registration/', data=user_registration_data)

    assert response.status_code == HTTP_400_BAD_REQUEST
    assert response.json() == {'contact_telephone': ['The phone number entered is not valid.']}




