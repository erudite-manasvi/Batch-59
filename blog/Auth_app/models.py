from django.db import models

# Create your models here.
class user(models.Model):
    fullname=models.CharField(max_length=100)
    country=models.CharField(max_length=50)