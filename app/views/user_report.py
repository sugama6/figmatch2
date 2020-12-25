from django.shortcuts import render
from app.models import *
from app.forms import *


def F200_ReportForm(request):
    return render(request, 'user_report/F200_ReportForm.html')


def F210_ReportComp(request):
    return render(request, 'user_report/F210_ReportComp.html')
