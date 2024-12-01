from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class Address(models.Model):
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        # If this isn’t given,
        # Django will use a munged version of the class name: CamelCase becomes camel case.
        verbose_name = "Adress"
        # The plural name for the object
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    objects = None
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
