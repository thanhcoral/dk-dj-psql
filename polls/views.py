from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail

from polls.forms import PatientForm
from polls.models import Patient

# Create your views here.
def home(request):
    patients = Patient.objects.all()
    context = {
        'data': patients
    }
    return render(request, 'home.html', context)

def addPatient(request):
    if request.method == 'POST':
        saveForm = PatientForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, 'Data has been added.')
    context = {
        'form': PatientForm
    }
    return render(request, 'add-patient.html', context)

def updatePatient(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        saveForm = PatientForm(request.POST, instance=patient)
        if saveForm.is_valid():
            saveForm.save()
            messages.success(request, 'Data has been updated.')
    context = {
        'form': PatientForm(instance=patient)
    }
    return render(request, 'update-patient.html', context)

def deletePatient(request, id):
    Patient.objects.filter(id=id).delete()
    return redirect('/')

def sendEmail(request,id):
    patient=Patient.objects.get(id=id) 
    send_mail(
        'Next Visit Reminder',
        'Your next visit is on '+ str(patient.visit_date),
        'admin@example.com',
        [patient.full_name],
        fail_silently=False,
    )
    messages.success(request,'Mail has been sent.')
    return redirect('/')