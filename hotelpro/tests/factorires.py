import factory
from faker import Faker
from pytest_factoryboy import register
from core.apps.account import models


fake = Faker()

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Account
        
        
        