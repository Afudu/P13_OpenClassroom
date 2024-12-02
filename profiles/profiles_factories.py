import factory
from django.contrib.auth.models import User
from faker import Faker
from profiles.models import Profile

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = factory.Faker("city")
