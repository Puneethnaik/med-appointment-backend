from django.db import models
from django.db.models import ForeignKey, IntegerField, AutoField
from doctor.models import Doctor
from hospital.models import Hospital
from patient.models import Patient
from django.contrib.auth.models import User

# Create your models here.
class WorksFor(models.Model):
    doctorId = ForeignKey(Doctor, on_delete=models.CASCADE)
    hospitalId = ForeignKey(Hospital, on_delete=models.CASCADE)
    id = AutoField(primary_key=True)

class Appointment(models.Model):
    doctorId = ForeignKey(Doctor, on_delete=models.CASCADE)
    hospitalId = ForeignKey(Hospital, on_delete=models.CASCADE)
    patientId = ForeignKey(Patient, on_delete=models.CASCADE)
    id=AutoField(primary_key=True)
