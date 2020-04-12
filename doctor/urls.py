from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView
urlpatterns = [
    path(r'doctor/', DoctorListCreateView.as_view()),
    path(r'doctor/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view()),
]