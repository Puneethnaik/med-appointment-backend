from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db.models import CharField, AutoField
# Create your models here.
class Hospital(models.Model):
    speciality = CharField(max_length=50)
    adress = CharField(max_length=50)
    id = AutoField(primary_key=True)