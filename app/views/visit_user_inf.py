from django.shortcuts import render
from app.models import *
from app.forms import *


def F370_visitUserProfile(request):
    return render(request, 'visit_user_inf/F370_visitUserProfile.html')
