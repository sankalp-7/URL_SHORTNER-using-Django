from re import M
from django.db import models
from django.forms import ModelChoiceField

# Create your models here.
class link(models.Model):
    long_url=models.CharField(max_length=1000)
    short_url=models.CharField(max_length=10)
