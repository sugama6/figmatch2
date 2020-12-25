from django.shortcuts import render
from app.models import *
from app.forms import *


def F250_BoardCateList(request):
    return render(request, 'board_inf/F250_BoardCateList.html')


def F260_BoardSearchResult(request):
    return render(request, 'board_inf/F260_BoardSearchResult.html')


def F270_BoardListByCate(request):
    return render(request, 'board_inf/F270_BoardListByCate.html')


def F280_BoardEdit(request):
    return render(request, 'board_inf/F280_BoardEdit.html')
