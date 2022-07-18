from typing import Dict, Any

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from main_app.apps.users.models import User

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'},
    )

    def create(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        validated_data['password'], _ = validated_data.pop('password1'), validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
        model = User
        fields = (
            'id',
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'patronymic',
            'birthday',
            'avatar',
            'contact_telephone',
            'extra_information',
        )

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if attrs['password1'] != attrs['password2']:
            raise ValidationError('Passwords don\'t match')

        return attrs


class UserUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            extra_kwargs = {
                'id': {'read_only': True},
                'username': {'read_only': True},
                'email': {'read_only': True},
            }
            model = User
            fields = (
                'id',
                'username',
                'email',
                'first_name',
                'last_name',
                'patronymic',
                'contact_telephone',
                'birthday',
                'avatar',
                'extra_information',
            )

