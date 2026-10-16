from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=12, unique=True, blank=True, null=True, verbose_name="Номер телефона")
    class Meta:
        db_table="auth_user"
        verbose_name= "Пользователи"
        verbose_name_plural="Пользователи"