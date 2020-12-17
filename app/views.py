from django.shortcuts render
from app.models import *
from app.forms import *

#TOP
def F010_Top(request):
    return render(request, 'user_top/F010_Top.html')

