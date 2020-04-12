from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from .permissions import IsCreationOrIsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .serializers import WorksForSerializer, AppointmentSerializer
from .models import WorksFor, Appointment
import json
# Create your views here.

class WorksForListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        works_for_objects = WorksFor.objects.all()
        serializer = WorksForSerializer(works_for_objects, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = WorksForSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class WorksForRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk, format=None):
        works_for_object = WorksFor.objects.all().filter(id=pk).first()
        if works_for_object is None:
            return Response({"error": "There is no record with id %d"%(pk)})
        serializer = WorksForSerializer(works_for_object)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        works_for_object = WorksFor.objects.all().filter(id=pk).first()
        if works_for_object is None:
            return Response({"error": "There is no record with id %d"%(pk)})
        serializer = WorksForSerializer(works_for_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        works_for_object = WorksFor.objects.all().filter(id=pk).first()
        if works_for_object is None:
            return Response({"error": "There is no record with id %d"%(pk)})
        serializer = WorksForSerializer(works_for_object)
        response = Response(serializer.data)
        works_for_object.delete()
        return response

class AppointmentListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class AppointmentRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, pk, format=None):
        appointment = Appointment.objects.all().filter(id=pk).first()
        if appointment is None:
            return Response({"error": "There is no record with id %d"%(pk)})
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        appointment = Appointment.objects.all().filter(id=pk).first()
        if appointment is None:
            return Response({"error": "There is no record with id %d"%(pk)})
        serializer = AppointmentSerializer(appointment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk, format=None):
        appointment = Appointment.objects.all().filter(id=pk).first()
        if appointment is None:
            return Response({"error": "There is no record with id %d"%(pk)})
        serializer = AppointmentSerializer(appointment)
        response = Response(serializer.data)
        appointment.delete()
        return response