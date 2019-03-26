from django import forms

from .models import Patient, Hospital, Treatment, PatientTreatment
from django.forms import ModelChoiceField

class CustomModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s. %s" % (obj.id, obj.name)

class CustomPatoentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s. %s %s" % (obj.id, obj.name, obj.last_name)        

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('name', 'last_name', 'age')


class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = ('name',)


class TreatmentForm(forms.ModelForm):

    hospital = CustomModelChoiceField(queryset=Hospital.objects.all())

    class Meta:
        model = Treatment
        fields = '__all__'

class PatientTreatmentForm(forms.ModelForm):

    patient = CustomPatoentModelChoiceField(queryset=Patient.objects.all())
    treatment = CustomModelChoiceField(queryset=Treatment.objects.all())

    class Meta:
        model = PatientTreatment
        fields = '__all__'