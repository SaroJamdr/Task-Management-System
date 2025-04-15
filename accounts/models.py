from django.db import models
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    choice= {
        'admin': 'Admin',
        'user': 'User',
    }
    role = models.CharField(max_length=10, choices=choice, default='user')
    email= models.EmailField(max_length=254, unique=True)
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['usename']
