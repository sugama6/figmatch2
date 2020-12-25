from django.shortcuts import render
from app.models import *
from app.forms import *


def F180_userPlanFigmatch(request):
    return render(request, 'user_join_fig/F180_userPlanFigmatch.html')


def F190_userPlanFigmatchDet(request):
    return render(request, 'user_join_fig/F190_userPlanFigmatchDet.html')
