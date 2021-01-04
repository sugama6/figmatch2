from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
from .common import *
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from figmatch import settings
from django.core.mail import EmailMessage

def F070_userPassForgot(request, status):
    params = {
        'status': status,
    }
    if request.method == 'POST':
        if status == 'complete':
            email = request.POST['email_address']
            try:
                #メールアドレスからユーザを取得
                user = Users.objects.get(email_address=email)
                #オールドパスワードの作成
                user.old_password = user.password
                user.save()
                token = get_random_chars()
                #パスワードリセットデータ作成
                password = passwordReset(
                    user = user,
                    token = token,
                    effective_date = timezone.now() + timedelta(days=1),
                    insert_time = common_current_time(),
                    update_time = common_current_time()
                )
                password.save()
                #メールの件名
                subject = 'パスワード再設定手続きのご確認'
                #メールの内容
                context = {
                    'user': user,
                    'token': token,
                }
                message = render_to_string('user_pass_reset/mail.txt', context, request)
                #メール送信元
                from_email = settings.DEFAULT_FROM_EMAIL
                #メール送信先
                recipient_list = [email]
                #Bcc設定
                bcc = [email]
                #メールの内容を作成・送信
                password_reset_mail = EmailMessage(subject, message, from_email, recipient_list, bcc)
                password_reset_mail.send()
                params = {
                    'status': 'complete',
                }
                return render(request, 'user_pass_reset/F070_userPassForgot.html', params)
            except:
                params = {
                    'status': 'complete',
                }
                return render(request, 'user_pass_reset/F070_userPassForgot.html', params)
    return render(request, 'user_pass_reset/F070_userPassForgot.html', params)


def F080_userPassResetting(request, token):
    pass_reset = passwordReset.objects.get(token=token)
    now = timezone.now()
    user = Users.objects.get(id=pass_reset.user.id)
    if request.method == 'GET':
        params = {
            'token': token,
            'del_flg': pass_reset.del_flg,
            'user': user,
        }
        #有効期限内 and 削除フラグが無かった場合
        if pass_reset.del_flg == 0 and now <= pass_reset.effective_date:
            #ページを表示したときに削除フラグを1にする    
            pass_reset.del_flg = 1
            pass_reset.save()
        return render(request, 'user_pass_reset/F080_userPassResetting.html', params)
        #POST送信時
    elif request.method == 'POST':
        #旧パスワードと新パスワードの作成
        user.password = common_hashing(request.POST['password'])
        user.lock_count = 0
        user.lock_flg = 0
        user.update_time = datetime.now()
        user.save()
        request.session['login_id'] = user.id
        return redirect('/F090_userPassResettingComp')
    return render(request, 'user_pass_reset/F080_userPassResetting.html', params)


def F090_userPassResettingComp(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    return render(request, 'user_pass_reset/F090_userPassResettingComp.html', params)
