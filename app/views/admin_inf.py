from django.shortcuts import render
from app.models import *
from app.forms import *


def F700_adminList(request):
    return render(request, 'admin_inf/F700_adminList.html')


def F710_adminDet(request):
    return render(request, 'admin_inf/F710_adminDet.html')


def F720_adminEdit(request):
    return render(request, 'admin_inf/F720_adminEdit.html')


def F730_adminMemReg(request):
    return render(request, 'admin_inf/F730_adminMemReg.html')


def F740_adminMemRegConf(request):
    return render(request, 'admin_inf/F740_adminMemRegConf.html')


def F750_adminMemRegComp(request):
    return render(request, 'admin_inf/F750_adminMemRegComp.html')
