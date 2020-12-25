from django.shortcuts import render
from app.models import *
from app.forms import *


def F680_adminReportList(request):
    return render(request, 'admin_report/F680_adminReportList.html')


def F690_adminReportDet(request):
    return render(request, 'admin_report/F690_adminReportDet.html')
