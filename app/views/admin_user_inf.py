from django.shortcuts import render
from app.models import *
from app.forms import *


def F550_adminUserList(request):
    return render(request, 'admin_user_inf/F550_adminUserList.html')


def F560_adminUserDet(request):
    return render(request, 'admin_user_inf/F560_adminUserDet.html')


def F570_adminUserEdit(request):
    return render(request, 'admin_user_inf/F570_adminUserEdit.html')


def F580_adminBoardFigList(request):
    return render(request, 'admin_user_inf/F580_adminBoardFigList.html')


def F590_adminBoardEdit(request):
    return render(request, 'admin_user_inf/F590_adminBoardEdit.html')


def F600_adminFigmatchEdit(request):
    return render(request, 'admin_user_inf/F600_adminFigmatchEdit.html')
