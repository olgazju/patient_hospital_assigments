from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.PatientListView.as_view(), name='patient'),
    path('patient/<int:pk>/', views.patient_details, name='patient_details'),
    path('patient/new/', views.patient_new, name='patient_new'),

    path('hospital/', views.HospitalListView.as_view(), name='hospital'),
    path('hospital/new/', views.hospital_new, name='hospital_new'),
    path('hospital/<int:pk>/', views.hospital_details, name='hospital_details'),

    path('treatment/', views.TreatmentListView.as_view(), name='treatment'),
    path('treatment/new/', views.treatment_new, name='treatment_new'),
    path('treatment/<int:pk>/', views.treatment_details, name='treatment_details'),

    path('patienttreatment/', views.PatientTreatmentListView.as_view(), name='patienttreatment'),
    path('patienttreatment/new/', views.patienttreatment_new, name='patienttreatment_new'),
    path('patienttreatment/<int:pk>/', views.patienttreatment_details, name='patienttreatment_details'),

]
