from django.shortcuts import render
from app.models import *
from app.forms import *


def F670_Notice(request):
    return render(request, 'notice/F670_Notice.html')
