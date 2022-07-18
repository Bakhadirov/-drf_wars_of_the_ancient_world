from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(blank=False)
    birthday = models.DateField(null=True)
    patronymic = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True, null=True, default=None)
    contact_telephone = PhoneNumberField()
    extra_information = models.TextField(blank=True)
