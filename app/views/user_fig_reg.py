from django.shortcuts import render
from app.models import *
from app.forms import *


def F290_userFigmatchReg(request):
    return render(request, 'user_fig_reg/F290_userFigmatchReg.html')


def F300_userFigmatchRegConf(request):
    return render(request, 'user_fig_reg/F300_userFigmatchRegConf.html')


def F310_userFigmatchRegComp(request):
    return render(request, 'user_fig_reg/F310_userFigmatchRegComp.html')
