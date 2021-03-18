from django import forms
from clinicalsApp.models import ClinicalData,Patients

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields='__all__'

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields='__all__'
