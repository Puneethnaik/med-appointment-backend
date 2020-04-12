from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import HospitalSerializer
from .models import Hospital
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.permissions import IsCreationOrIsAuthenticatedOrReadOnly
import rest_framework.status as statuses
# Create your views here.
class HospitalListCreateView(APIView):
    permission_classes = [IsCreationOrIsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        serializer = HospitalSerializer(data=Hospital.objects.all(), many=True)
        serializer.is_valid()
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        serializer = HospitalSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class HospitalRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def put(self, request, pk, format=None):
        data = request.data
        hospital = Hospital.objects.all().filter(id=pk).first()
        serializer = HospitalSerializer(hospital, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request, pk, format=None):
        hospital = Hospital.objects.all().filter(id=pk).first()
        serializer = HospitalSerializer(hospital)
        # serializer.is_valid()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        hospital = Hospital.objects.all().filter(id=pk)
        if not hospital:
            response = {"errorMessage": "There is no hospital with id=%d"%(pk)}
            return Response(response, status=statuses.HTTP_400_BAD_REQUEST)
        else:
            serializer = HospitalSerializer(hospital.first())
            hospital.delete()
            return Response(serializer.data)
