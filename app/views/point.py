from django.shortcuts import render
from app.models import *
from app.forms import *


def F610_awardPoint(request):
    return render(request, 'point/F610_awardPoint.html')


def F620_awardPointComp(request):
    return render(request, 'point/F620_awardPointComp.html')
