from django.shortcuts import render
from rest_framework.views import APIView
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.permissions import IsCreationOrIsAuthenticatedOrReadOnly
class PatientListCreateView(APIView):
    permission_classes = [IsCreationOrIsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        patient_list = Patient.objects.all()
        serializer = PatientSerializer(data=patient_list, many=True)
        serializer.is_valid()
        return Response(serializer.data)
    def post(self, request, format=None):
        data = request.data
        serializer = PatientSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PatientRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        data = request.data
        patient = Patient.objects.all().filter(id=pk)
        serializer = PatientSerializer(patient, data=data, partial=True)
        is_valid = serializer.is_valid()
        print(serializer.errors)
        serializer.save()

        return Response(serializer.data)
    def get(self, request, pk, format=None):
        patient = Patient.objects.all().filter(id=pk).first()
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        patient = Patient.objects.all().filter(id=pk).first()
        serializer = PatientSerializer(patient)
        patient.delete()
        return Response(serializer.data)
        
