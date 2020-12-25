from django.shortcuts import render
from app.models import *
from app.forms import *


def F470_Settings(request):
    return render(request, 'user_setting/F470_Settings.html')


def F480_passChange(request):
    return render(request, 'user_setting/F480_passChange.html')


def F490_passChangeComp(request):
    return render(request, 'user_setting/F490_passChangeComp.html')


def F500_Exit(request):
    return render(request, 'user_setting/F500_Exit.html')


def F510_ExitConf(request):
    return render(request, 'user_setting/F510_ExitConf.html')


def F520_ExitComp(request):
    return render(request, 'user_setting/F520_ExitComp.html')
