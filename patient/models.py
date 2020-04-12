from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db.models import DateField, CharField, AutoField
# Create your models here.
class Patient(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = DateField()
    gender = CharField(max_length=1)
    mobileNumber = CharField(max_length=12)
    id = AutoField(primary_key=True)