from django.shortcuts import render
from app.models import *
from app.forms import *
from .common import *


def F010_Top(request):
    return render(request, 'user_top/F010_Top.html')


def F020_userLogin(request):
    params = {
        'error': '',
    }
    #POST送信時
    if request.method == 'POST':        
        email_address = request.POST['email_address']        
        #パスワードハッシュ化
        password = common_hashing(request.POST['password'])        
        #該当するユーザーがいる時
        try:
            user = Users.objects.get(email_address=email_address, password=password, exit=0, suspension=0)            
            #ロックのチェック
            if user.lock_flg == 1:
                params['error'] = 'このユーザーはロックされています'
                return render(request, 'user_top/F020_userLogin.html', params)
            #ログイン成功時
            else:
                user.lock_count = 0
                user.save()
                request.session.clear()
                request.session['login_id'] = user.id
                return redirect('/F030_userTop')
        #該当するユーザーがいない時
        except:
            #ユーザーIDのみあっている時
            if Users.objects.filter(email_address=email_address).count() == 1:
                failed = Users.objects.get(email_address=email_address)
                failed.lock_count += 1
                failed.save()
                #ロックカウントが5以上の時
                if failed.lock_count >= 5:
                    failed.lock_flg = 1
                    failed.save()
                    params['error'] = 'ロックされました'
                    return render(request, 'user_top/F020_userLogin.html', params)
            #IDもパスワードも一致しない時
            params['error'] = 'メールアドレスもしくはパスワードが違います'
            return render(request, 'user_top/F020_userLogin.html', params)
    return render(request, 'user_top/F020_userLogin.html', params)


def F030_userTop(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    return render(request, 'user_top/F030_userTop.html', params)
