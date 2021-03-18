from django.shortcuts import render
from clinicalsApp.models import Patients, ClinicalData
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
from django.shortcuts import render, redirect
# Create your views here.
class PatientListView(ListView):
    model=Patients

class PatientCreateView(CreateView):
    model=Patients
    success_url = reverse_lazy('index')
    fields=('firstName', 'lastName', 'age')

class PatientUpdateView(UpdateView):
    model=Patients
    success_url = reverse_lazy('index')
    fields=('firstName', 'lastName', 'age')


class PatientDeleteView(DeleteView):
    model=Patients
    success_url = reverse_lazy('index')

def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patients.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {'form':form, 'patient':patient})

def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData=[]
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                feetToMeters = float(heightAndWeight[0]) * 0.4536
                BMI = (float(heightAndWeight[1])) / (feetToMeters * feetToMeters)

                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.ComponentValue = BMI
                responseData.append(bmiEntry)
            responseData.append(eachEntry)
            print("BMI", bmiEntry.ComponentValue)
    return render(request, 'clinicalsApp/generateReport.html', {'data':responseData})
