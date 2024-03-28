from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    User = models.OneToOneField(User,null=True, blank=True)
