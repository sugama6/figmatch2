from django.shortcuts import render
from app.models import *
from app.forms import *


def F760_identification(request):
    return render(request, 'identification/F760_identification.html')


def F770_identificationDet(request):
    return render(request, 'identification/F770_identificationDet.html')
