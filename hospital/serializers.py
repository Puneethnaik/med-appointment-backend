from rest_framework.serializers import Serializer, CharField, IntegerField
from .models import Hospital

class HospitalSerializer(Serializer):
    speciality = CharField(max_length=50)
    adress = CharField(max_length=50)
    id = IntegerField(required=False)
    def create(self, validated_data):
        return Hospital.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.speciality = validated_data.get("speciality")
        instance.adress = validated_data.get("adress")
        instance.save()
        return instance
