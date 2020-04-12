from rest_framework.serializers import Serializer , PrimaryKeyRelatedField, DateTimeField, CharField, IntegerField, EmailField
from django.contrib.auth.models import User
from .models import WorksFor, Appointment
from doctor.models import Doctor
from hospital.models import Hospital
from patient.models import Patient
import datetime
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
    start = DateTimeField(input_formats=["%d-%m-%Y %H:%M:%S"])
    end = DateTimeField(input_formats=["%d-%m-%Y %H:%M:%S"])
    id=IntegerField(required=False)
    def create(self, validated_data):
        # startTime = datetime.strptime(validated_data.get("start"), )
        # validated_data["start"] = startTime
        # endTime = datetime.strptime(validated_data.get("start"), "%d-%m-%Y %H:%M:%S %z")
        # validated_data["end"] = endTime
        return Appointment.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.hospitalId = validated_data.get('hospitalId')
        instance.patientId = validated_data.get('patientId')
        instance.doctorId = validated_data.get('doctorId')
        # startTime = datetime.strptime(validated_data.get("start"), "%d-%m-%Y %H:%M:%S %z")
        instance.start = validated_data.get("start"),
        # endTime = datetime.strptime(validated_data.get("start"), "%d-%m-%Y %H:%M:%S %z")
        instance.end = validated_data.get("end")
        instance.save()
        return instance


'''
from api.serializers import AppointmentSerializer

data = {'doctorId': 5, 'hospitalId': 12, 'patientId': 2, 'start': '20-02-2020 18:25:03', 'end': '20-02-2020 19:25:03'}
serializer = AppointmentSerializer(data=data)
serializer.is_valid()
'''