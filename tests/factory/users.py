import datetime
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText, FuzzyDate
from faker import Faker

from main_app.apps.users.models import User

fake = Faker()


class UserFactory(DjangoModelFactory):
    email = fake.email()
    username = FuzzyText()
    password = FuzzyText()
    first_name = FuzzyText()
    last_name = FuzzyText()
    patronymic = FuzzyText()
    birthday = FuzzyDate(start_date=datetime.date(1990, 1, 1), end_date=datetime.date(1999, 1, 1))
    contact_telephone = fake.phone_number()
    is_active = True
    is_staff = False
    extra_information = FuzzyText()



    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        user = cls._get_manager(model_class)
        if 'is_superuser' in kwargs:
            return user.create_superuser(*args, **kwargs)
        else:
            return user.create_user(*args, **kwargs)

    class Meta:
        model = User

