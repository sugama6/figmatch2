from django.shortcuts import render
from app.models import *
from app.forms import *


def F220_userBoardReg(request):
    return render(request, 'user_board_reg/F220_userBoardReg.html')


def F230_userBoardRegConf(request):
    return render(request, 'user_board_reg/F230_userBoardRegConf.html')


def F240_userBoardRegComp(request):
    return render(request, 'user_board_reg/F240_userBoardRegComp.html')
