from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add any additional fields you require for your user model
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)
    pass