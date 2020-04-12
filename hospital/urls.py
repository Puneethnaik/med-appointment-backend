from django.urls import path
from .views import HospitalListCreateView, HospitalRetrieveUpdateDestroyView
urlpatterns = [
    path(r'hospital/', HospitalListCreateView.as_view()),
    path(r'hospital/<int:pk>/', HospitalRetrieveUpdateDestroyView.as_view()),
]