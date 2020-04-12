from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField
from django.db.models import DateField, CharField, CharField, IntegerField, AutoField
# Create your models here.
class Doctor(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    qualification = CharField(max_length=50)
    specialisation = CharField(max_length=50)
    gender = CharField(max_length=1)
    title = CharField(max_length=50)
    experience = IntegerField()
    id = AutoField(primary_key=True)
    def __str__(self):
        return "Doctor <%s>"%(self.user.username)
    