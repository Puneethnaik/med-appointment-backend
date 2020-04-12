from django.urls import path
from .views import PatientListCreateView, PatientRetrieveUpdateDestroyView
urlpatterns = [
    path(r'patient/', PatientListCreateView.as_view()),
    path(r'patient/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view()),
]