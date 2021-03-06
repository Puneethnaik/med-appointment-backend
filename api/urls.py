from django.urls import path, include
from api.views import  WorksForListCreateView, AppointmentRetrieveByHospitalView ,AppointmentRetrieveByDoctorView ,WorksForRetrieveUpdateDestroyView, AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path(r'doctor/', include('doctor.urls')),
    path(r'patient/', include('patient.urls')),
    path(r'hospital/', include('hospital.urls')),
    path(r'worksfor/worksfor/', WorksForListCreateView.as_view()),
    path(r'worksfor/worksfor/<int:pk>/', WorksForRetrieveUpdateDestroyView.as_view()),
    path(r'appointment/appointment/', AppointmentListCreateView.as_view()),
    path(r'appointment/appointment/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view()),
    path(r'appointment/doctor/<int:doctorId>/', AppointmentRetrieveByDoctorView.as_view()),
    path(r'appointment/hospital/<int:hospitalId>/', AppointmentRetrieveByHospitalView.as_view()),
    path(r'api-token-auth/', TokenObtainPairView.as_view()),
]