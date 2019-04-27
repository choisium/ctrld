from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 필요한 모델: User, Profile(if needed), Genre, Calendar, Event, Schedule

class User(AbstractUser):
    pass