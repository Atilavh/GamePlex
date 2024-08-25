from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.

class Registration(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    full_name = models.CharField(max_length=20, verbose_name='نام کامل')
    username = models.CharField(max_length=100, verbose_name='نام کاربری', unique=True)
    phone_number = models.CharField(max_length=100, verbose_name='شماره همراه', unique=True)
    email = models.EmailField(max_length=100, verbose_name='ایمیل', unique=True)
    email_active_code = models.CharField(max_length=48, verbose_name='کد فعال کننده')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.full_name

