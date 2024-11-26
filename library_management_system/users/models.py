from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    personal_number = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    full_name = models.CharField(max_length=100)

    username = None

    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['personal_number', 'birth_date', 'full_name']

    def __str__(self):
        return self.full_name or self.email
