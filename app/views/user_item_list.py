from django.shortcuts import render
from app.models import *
from app.forms import *


def F140_myFigmatchDet(request):
    return render(request, 'user_item_list/F140_myFigmatchDet.html')


def F150_myBoardDet(request):
    return render(request, 'user_item_list/F150_myBoardDet.html')


def F160_myBoardEdit(request):
    return render(request, 'user_item_list/F160_myBoardEdit.html')


def F170_myFigmatchEdit(request):
    return render(request, 'user_item_list/F170_myFigmatchEdit.html')
