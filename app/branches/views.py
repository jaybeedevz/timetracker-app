from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse

from doctors.models import Physician
from doctors.models import Schedule

def index(request):

    physicians = Physician.objects.all()
    schedules = Schedule.objects.all()

    context = {
        'physicians': physicians,
        'schedules': schedules
    }
    return render(request, 'pages/index.html', context)	    


def smne(request):

    smne_physicians = Physician.objects.filter(clinic__branch_name="SM North Edsa")
    smne_monday = Schedule.objects.filter(schedule_day="Monday")

    context ={
        'smne_physicians': smne_physicians,
        'smne_monday': smne_monday
    }

    return render(request, 'pages/smne.html', context)

def shang(request):
    return render(request, 'pages/shang.html')

def rpm(request):
    return render(request, 'pages/rpm.html')

def filomena(request):
    return render(request, 'pages/filomena.html')

def venice(request):
    return render(request, 'pages/venice.html')

def dd(request):
    return render(request, 'pages/dd.html')

def alabang(request):
    return render(request, 'pages/alabang.html')

def cybergate(request):
    return render(request, 'pages/cybergate.html')

def galleria(request):
    return render(request, 'pages/galleria.html')