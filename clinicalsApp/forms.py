from django import forms
from clinicalsApp.models import ClinicalData, Patient

class PatientForm(forms.ModelForm)
    class Meta:
        model = Patients
        field='__all__'

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        field='__all__'
