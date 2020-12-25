from django.shortcuts import render
from app.models import *
from app.forms import *


def F400_shopTop(request):
    return render(request, 'shop/F400_shopTop.html')


def F410_PointShop(request):
    return render(request, 'shop/F410_PointShop.html')


def F420_GiftShop(request):
    return render(request, 'shop/F420_GiftShop.html')
