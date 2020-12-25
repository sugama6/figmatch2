from django.shortcuts import render
from app.models import *
from app.forms import *


def F070_userPassForgot(request):
    return render(request, 'user_pass_reset/F070_userPassForgot.html')


def F080_userPassResetting(request):
    return render(request, 'user_pass_reset/F080_userPassResetting.html')


def F090_userPassResettingComp(request):
    return render(request, 'user_pass_reset/F090_userPassResettingComp.html')
