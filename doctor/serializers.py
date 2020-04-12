from rest_framework.serializers import Serializer, CharField, IntegerField
from .models import Doctor
from django.contrib.auth.models import User
from api.serializers import UserSerializer

class DoctorSerializer(Serializer):
    user = UserSerializer()
    qualification = CharField(max_length=50)
    specialisation = CharField(max_length=50)
    gender = CharField(max_length=1)
    title = CharField(max_length=50)
    experience = IntegerField()
    id = IntegerField(required=False)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        return Doctor.objects.create(user=user, **validated_data)
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.all().filter(username = user_data.get('username')).first()
        user.first_name = user_data['first_name']
        user.last_name = user_data.get('last_name')
        user.email = user_data.get('email')
        user.save()
        instance = instance
        instance.user = user
        instance.qualification = validated_data.get("qualification")
        instance.experience = validated_data.get("experience")
        instance.specialisation = validated_data.get("specialisation")
        instance.gender = validated_data.get("gender")
        instance.title = validated_data.get("title")
        instance.save()
        return instance