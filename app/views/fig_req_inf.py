from django.shortcuts import render
from app.models import *
from app.forms import *


def F630_FigmatchRequest(request):
    return render(request, 'fig_req_inf/F630_FigmatchRequest.html')


def F640_FigmatchRequestDet(request):
    return render(request, 'fig_req_inf/F640_FigmatchRequestDet.html')
