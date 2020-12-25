from django.shortcuts import render
from app.models import *
from app.forms import *


def F100_myProfileDet(request):
    return render(request, 'user_profile_inf/F100_myProfileDet.html')


def F101_identification_app(request):
    return render(request, 'user_profile_inf/F101_identification_app.html')


def F110_myProfileEdit(request):
    return render(request, 'user_profile_inf/F110_myProfileEdit.html')
