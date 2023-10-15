from ..apps.account import models as account_models
import factory
from faker import Faker
from pytest_factoryboy import register


fake = Faker()


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = account_models.CustomUser

    phone_number = fake.phone_number()
    phone_number = (
        phone_number.replace("-", "")
        .replace("(", "")
        .replace(")", "")
        .replace(" ", "")
        .replace(".", "")
        .replace("+", "")
    )
    phone_number = f"09{phone_number[:9]}"
    username = fake.lexify(text="user_name_?????")
    first_name = fake.first_name()
    last_name = fake.last_name()


register(AccountFactory)
