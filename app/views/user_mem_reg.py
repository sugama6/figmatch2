from django.shortcuts import render
from app.models import *
from app.forms import *
from .common import *


def F040_userMemReg(request):
    params = {
        'form': InitialRegistrationForm()
    }
    if request.method == 'POST':
        params = {
            'form': InitialRegistrationForm(request.POST)
        }
    return render(request, 'user_mem_reg/F040_userMemReg.html', params)


def F050_userMemRegConf(request):
    if request.method == 'GET':
        return redirect('/F040_userMemReg')
    if request.method == 'POST':
        form = InitialRegistrationForm(request.POST)
        if form.is_valid():
            #アカウント名の重複チェック
            if Users.objects.filter(acount_name=request.POST['acount_name']).count() == 1:
                params = {
                    'form': form,
                    'acount_error': 'このアカウント名は既に使用されています'
                }
                return render(request, 'user_mem_reg/F040_userMemReg.html', params)
            #メールアドレスの重複のチェック
            elif Users.objects.filter(email_address=request.POST['email_address']).count() == 1:
                params = {
                    'form': form,
                    'email_error': 'このメールアドレスは既に登録されています'
                }
                return render(request, 'user_mem_reg/F040_userMemReg.html', params)
            #パスワードのチェック
            elif request.POST['password'] != request.POST['password2']:
                password_error = 'パスワードが一致しません'
                params = {
                    'form': form,
                    'password_error': password_error,
                }
                return render(request, 'user_mem_reg/F040_userMemReg.html', params)
        else :
            params = {
                'form': InitialRegistrationForm(request.POST)
            }
            return render(request, 'user_mem_reg/F040_userMemReg.html', params)
        params = {
            'data': request.POST
        }
    return render(request, 'user_mem_reg/F050_userMemRegConf.html', params)


def F060_userMemRegComp(request):
    if request.method == 'POST':
        try:
            user = Users(
                user_name = request.POST['user_name'],
                password = common_hashing(request.POST['password']),
                acount_name = request.POST['acount_name'],
                email_address = request.POST['email_address'],
                insert_time = common_current_time(),
                update_time = common_current_time(),
            )
            user.save()
            id = Users.objects.get(email_address=request.POST['email_address'])
            create_user_session(request, id.id)
        except:
            return redirect('/F030_userTop')
    return render(request, 'user_mem_reg/F060_userMemRegComp.html')
