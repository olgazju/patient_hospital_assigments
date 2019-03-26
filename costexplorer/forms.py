from django import forms

from .models import Patient, Hospital

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('name', 'last_name', 'age')


class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = ('name',)