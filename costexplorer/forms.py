from django import forms

from .models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('name', 'last_name', 'age')