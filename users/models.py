from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser): # customuser is inheriting from abstract user because abstract user is abstract class
    phone_number=models.CharField(max_length=12)
