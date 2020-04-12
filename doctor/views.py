from django.shortcuts import render
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.permissions import IsCreationOrIsAuthenticatedOrReadOnly
# Create your views here.
class DoctorListCreateView(APIView):
    permission_classes = [IsCreationOrIsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        doctor_list = Doctor.objects.all()
        serializer = DoctorSerializer(data=doctor_list, many=True)
        serializer.is_valid()
        return Response(serializer.data)
    def post(self, request, format=None):
        data = request.data
        serializer = DoctorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class DoctorRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        data = request.data
        doctor = Doctor.objects.all().filter(id=pk).first()
        serializer = DoctorSerializer(doctor, data=data, partial=True)
        is_valid = serializer.is_valid()
        print(serializer.errors)
        serializer.save()

        return Response(serializer.data)
    def get(self, request, pk, format=None):
        doctor = Doctor.objects.all().filter(id=pk).first()
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        doctor = Doctor.objects.all().filter(id=pk).first()
        serializer = DoctorSerializer(doctor)
        doctor.delete()
        return Response(serializer.data)
        