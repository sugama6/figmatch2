from django.shortcuts import render
from app.models import *
from app.forms import *


def F320_FigmatchList(request):
    return render(request, 'fig_inf/F320_FigmatchList.html')


def F330_FigmatchSearch(request):
    return render(request, 'fig_inf/F330_FigmatchSearch.html')


def F340_FigmatchDet(request):
    return render(request, 'fig_inf/F340_FigmatchDet.html')


def F350_FigmatchApp(request):
    return render(request, 'fig_inf/F350_FigmatchApp.html')


def F360_FigmatchAppComp(request):
    return render(request, 'fig_inf/F360_FigmatchAppComp.html')
