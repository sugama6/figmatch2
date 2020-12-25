from django.shortcuts import render
from app.models import *
from app.forms import *


def F120_myGoodBoardList(request):
    return render(request, 'user_good_board/F120_myGoodBoardList.html')


def F130_myGoodBoardDet(request):
    return render(request, 'user_good_board/F130_myGoodBoardDet.html')
