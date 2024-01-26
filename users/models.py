from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    current_half_year = models.ForeignKey('calander.HalfYear', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="نیمسال جاری")