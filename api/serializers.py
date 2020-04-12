from rest_framework.serializers import Serializer , PrimaryKeyRelatedField, CharField, IntegerField, EmailField
from django.contrib.auth.models import User
from .models import WorksFor, Appointment
from doctor.models import Doctor
from hospital.models import Hospital
from patient.models import Patient
class UserSerializer(Serializer):
    username = CharField(max_length=150)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=150)
    password = CharField(max_length=150, write_only=True)
    email = EmailField()
    id=IntegerField(required=False)

class WorksForSerializer(Serializer):
    doctorId = PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    hospitalId = PrimaryKeyRelatedField(queryset=Hospital.objects.all())
    id = IntegerField(required=False)
    def create(self, validated_data):
        print("The validated data is", validated_data)
        works_for_object = WorksFor.objects.create(**validated_data)
        works_for_object.save()
        return works_for_object
    def update(self, instance, validated_data):
        instance.hospitalId = validated_data.get('hospitalId', None)
        instance.doctorId = validated_data.get('doctorId', None)
        instance.save()
        return instance
    
class AppointmentSerializer(Serializer):
    doctorId = PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    hospitalId = PrimaryKeyRelatedField(queryset=Hospital.objects.all())
    patientId = PrimaryKeyRelatedField(queryset=Patient.objects.all())
    id=IntegerField(required=False)
    def create(self, validated_data):
        return Appointment.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.hospitalId = validated_data.get('hospitalId')
        instance.patientId = validated_data.get('patientId')
        instance.doctorId = validated_data.get('doctorId')
        instance.save()
        return instance
