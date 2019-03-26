from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/', views.PatientListView.as_view(), name='patient'),

    path('patient/<int:pk>/', views.patient_details, name='patient_details'),
    path('patient/new/', views.patient_new, name='patient_new'),
    #path('hospital/', views.hospital, name='hospital'),
    #path('treatment/', views.treatment, name='treatment'),
    #path('tfp/', views.tfp, name='tfp'),
    #path('summary/', views.summary, name='summary'),
]
