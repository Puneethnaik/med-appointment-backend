from django.urls import path, include
from api.views import  WorksForListCreateView, AppointmentRetrieveByDoctorView ,WorksForRetrieveUpdateDestroyView, AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path(r'doctor/', include('doctor.urls')),
    path(r'patient/', include('patient.urls')),
    path(r'hospital/', include('hospital.urls')),
    path(r'worksfor/worksfor/', WorksForListCreateView.as_view()),
    path(r'worksfor/worksfor/<int:pk>/', WorksForRetrieveUpdateDestroyView.as_view()),
    path(r'appointment/appointment/', AppointmentListCreateView.as_view()),
    path(r'appointment/appointment/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view()),
    path(r'appointment/doctor/<int:doctorId>/', AppointmentRetrieveByDoctorView.as_view()),
    path(r'api-token-auth/', obtain_jwt_token),
]