from rest_framework.serializers import Serializer, CharField, DateField, IntegerField
from api.serializers import UserSerializer
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(Serializer):
    user = UserSerializer()
    date_of_birth = DateField()
    gender = CharField(max_length=1)
    mobileNumber = CharField(max_length=12)
    id=IntegerField(required=False)
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Patient.objects.create(user=user, **validated_data)
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.all().filter(username=user_data.get("username")).first()
        user.first_name = user_data['first_name']
        user.last_name = user_data.get('last_name')
        user.email = user_data.get('email')
        user.save()
        instance = instance.first()
        instance.user = user
        instance.date_of_birth = validated_data.get("date_of_birth")
        instance.gender = validated_data.get("gender")
        instance.mobileNumber = validated_data.get("mobileNumber")
        instance.save()
        return instance