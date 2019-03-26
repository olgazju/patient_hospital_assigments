from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Patient, Hospital, Treatment, PatientTreatment
from .forms import PatientForm, HospitalForm, TreatmentForm, PatientTreatmentForm

def index(request):
    return render(request, 'costexplorer/index.html')


class PatientListView(generic.ListView):
    model = Patient

def patient_details(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'costexplorer/patient_details.html', context={'patient': patient})

def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return redirect('patient_details', pk=patient.id)
    else:
        form = PatientForm()
    return render(request, 'costexplorer/patient_edit.html', {'form': form})


class HospitalListView(generic.ListView):
    model = Hospital

def hospital_details(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'costexplorer/hospital_details.html', context={'hospital': hospital})

def hospital_new(request):
    if request.method == "POST":
        form = HospitalForm(request.POST)
        if form.is_valid():
            hospital = form.save(commit=False)
            hospital.save()
            return redirect('hospital_details', pk=hospital.id)
    else:
        form = HospitalForm()
    return render(request, 'costexplorer/hospital_edit.html', {'form': form})


class TreatmentListView(generic.ListView):
    model = Treatment

def treatment_details(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    return render(request, 'costexplorer/treatment_details.html', context={'treatment': treatment})

def treatment_new(request):
    if request.method == "POST":
        form = TreatmentForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.save()
            return redirect('treatment_details', pk=treatment.id)
    else:
        form = TreatmentForm()
    return render(request, 'costexplorer/treatment_edit.html', {'form': form})


class PatientTreatmentListView(generic.ListView):
    model = PatientTreatment

def patienttreatment_details(request, pk):
    patienttreatment = get_object_or_404(PatientTreatment, pk=pk)
    return render(request, 'costexplorer/patienttreatment_details.html', context={'patienttreatment': patienttreatment})

def patienttreatment_new(request):
    if request.method == "POST":
        form = PatientTreatmentForm(request.POST)
        if form.is_valid():
            patienttreatment = form.save(commit=False)
            patienttreatment.save()
            return redirect('patienttreatment_details', pk=patienttreatment.id)
    else:
        form = PatientTreatmentForm()
    return render(request, 'costexplorer/patienttreatment_edit.html', {'form': form})