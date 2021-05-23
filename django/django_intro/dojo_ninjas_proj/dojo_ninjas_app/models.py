from django.db import models
from django.db.models.fields import IntegerField

class Dojo(models.Model):

    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    additional=models.TextField()

class Ninja(models.Model):
    dojo=models.ForeignKey(Dojo,related_name="ninjas",on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)


# Create your models here.
