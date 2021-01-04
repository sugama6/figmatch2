from django.shortcuts import render
from app.models import *
from app.forms import *


def F430_Notice(request):
    return render(request, 'gloval_nav/F430_Notice.html')


def F440_TermsOfService(request):
    return render(request, 'gloval_nav/F440_TermsOfService.html')


def F450_Inquiry(request):
    return render(request, 'gloval_nav/F450_Inquiry.html')


def F460_InquiryComp(request):
    return render(request, 'gloval_nav/F460_InquiryComp.html')
