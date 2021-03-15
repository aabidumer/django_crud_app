from django.shortcuts import render
from clinicalsApp.models import Patients
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

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
