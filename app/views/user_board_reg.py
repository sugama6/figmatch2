from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
from .common import *

def F220_userBoardReg(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
        'form': CreateBoardForm(),
    }
    if request.method == 'POST':
        params = {
            'form': CreateBoardForm(request.POST),
            'user': user,
        }
    return render(request, 'user_board_reg/F220_userBoardReg.html', params)


def F230_userBoardRegConf(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    if request.method == 'GET':
        return redirect('/F220_userBoardReg')
    if request.method == 'POST':
        thumbnail = common_uploaded_file(request.FILES['thumbnail'], '/thumbnail/' + str(user.id) + '/')
        if request.FILES.get('wallpaper') != None:
            wallpaper = common_uploaded_file(request.FILES['wallpaper'], '/wallpaper/' + str(user.id) + '/')
        else :
            wallpaper = ''
        params = {
            'request': request.POST,
            'thumbnail': thumbnail,
            'wallpaper': wallpaper,
            'user': user
        }
        return render(request, 'user_board_reg/F230_userBoardRegConf.html', params)


def F240_userBoardRegComp(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    if request.method == 'POST':
        if request.POST['category2']:
            category2 = request.POST['category2']
        else:
            category2 = ''
        if request.POST['category3']:
            category3 = request.POST['category3']
        else:
            category3 = ''
        board = Board(
            user = Users.objects.get(id=user.id),
            board_title = request.POST['board_title'],
            category1 = request.POST['category1'],
            category2 = category2,
            category3 = category3,
            participation_conditions = request.POST['participation_conditions'], 
            thumbnail = request.POST['thumbnail'], 
            wallpaper = request.POST['wallpaper'], 
            introduction = request.POST['introduction'], 
            release_flg = request.POST['release_flg'], 
            insert_time = common_current_time(),
            update_time = common_current_time(),
        )
        board.save()
    return render(request, 'user_board_reg/F240_userBoardRegComp.html', params)
