
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from  django.conf import settings
from datetime import timedelta

import random
def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)

SEX = (
    ('G', 'Gender'),
    ('M', 'Male'),
    ('F', 'Female'),
)

LEVEL = (
    ('Promo','Promo'),
    ('Silver','Silver'),
    ('Gold', 'Gold'),
    ('Platinum', 'Platinum')
)
#manager for our custom model 

class UserManager(BaseUserManager):
    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    """Custom user class inheriting AbstractBaseUser class."""
    
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone = models.CharField(max_length=50)
    stage = models.CharField(choices=LEVEL, default="Promo", max_length=9)
    profile_value = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    dob = models.DateField(default=return_date_time)
    address = models.CharField(max_length=100) 
    postal_code = models.CharField(max_length=10)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email

class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    query = models.TextField()

    class Meta:
        verbose_name_plural = "Contact Us"
