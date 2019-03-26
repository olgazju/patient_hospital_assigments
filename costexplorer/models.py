from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator

my_validator = RegexValidator(r'^[a-zA-Z]+$', "Your string should contain only letters.")

class Patient(models.Model):
    name = models.CharField(max_length=200, validators=[my_validator])
    last_name = models.CharField(max_length=200, validators=[my_validator])
    age = models.IntegerField(validators=[
            MaxValueValidator(150),
            MinValueValidator(0)])


class Hospital(models.Model):
    name = models.CharField(max_length=200)

class Treatment(models.Model):
	hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	price = models.FloatField(validators=[
            MinValueValidator(0)])


class PatientTreatment(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)