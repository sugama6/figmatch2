from django.shortcuts import render
from app.models import *
from app.forms import *
from .common import *

def F100_myProfileDet(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    user_data = Users.objects.filter(id=login_id)
    params = {
        'user': user,
        'user_data': user_data,
        'id': login_id
    }
    return render(request, 'user_profile_inf/F100_myProfileDet.html', params)


def F101_identification_app(request):
    
    return render(request, 'user_profile_inf/F101_identification_app.html')


def F110_myProfileEdit(request, id, status):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('sex_flg') == 'on':
            sex_flg = True
        else :
            sex_flg = False
        if request.POST.get('age_flg') == 'on':
            age_flg = True
        else :
            age_flg = False
        form = userProfileForm(request.POST, instance=user)
        if form.is_valid():
            if request.FILES.get('user_image') != None:
                user_image = common_uploaded_file(request.FILES['user_image'], '/user_image/' + str(login_id) + '/')
            else :
                user_image = user.user_image
            category = request.POST.getlist('category')
            form = form.save(commit=True)
            form.user_image = user_image
            form.age_flg = age_flg
            form.sex_flg = sex_flg
            form.category = category
            form.update_time = common_current_time()
            form.save()
            status = 'complete'
        else :
            status = 'active'
        params = {
            'user': user,
            'form': userProfileForm(request.POST),
            'id': id,
            'status': status,
        }
        return render(request, 'user_profile_inf/F110_myProfileEdit.html', params)        
    params = {
        'user': user,
        'form': userProfileForm(instance=user),
        'id': id,
        'status': status,
    }
    return render(request, 'user_profile_inf/F110_myProfileEdit.html', params)
