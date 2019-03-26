from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Patient
from .forms import PatientForm

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