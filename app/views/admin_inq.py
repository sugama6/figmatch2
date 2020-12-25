from django.shortcuts import render
from app.models import *
from app.forms import *


def F650_adminInquiryList(request):
    return render(request, 'admin_inq/F650_adminInquiryList.html')


def F660_adminInquiryDet(request):
    return render(request, 'admin_inq/F660_adminInquiryDet.html')
