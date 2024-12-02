"""pytest-factoryboy makes it easy to combine factory approach
to the test setup with the dependency injection,
heart of the pytest fixtures."""

import factory
from faker import Faker
from lettings.models import Address, Letting

faker = Faker()


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    number = factory.Faker("random_int", min=1, max=9999)
    street = factory.Faker("street_name")
    city = factory.Faker("city")
    state = factory.Faker("state_abbr")
    zip_code = factory.Faker("random_int", min=10000, max=99999)
    country_iso_code = factory.Faker("country_code")


class LettingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Letting

    title = factory.Faker("sentence", nb_words=4)
    address = factory.SubFactory(AddressFactory)
