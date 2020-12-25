from django.shortcuts import render
from app.models import *
from app.forms import *


def F530_adminLogin(request):
    return render(request, 'admin_top/F530_adminLogin.html')


def F540_adminTop(request):
    return render(request, 'admin_top/F540_adminTop.html')
