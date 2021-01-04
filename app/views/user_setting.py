from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
from .common import *
from django.template.loader import render_to_string
from figmatch import settings
from django.core.mail import EmailMessage
from random import random

def F470_Settings(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    return render(request, 'user_setting/F470_Settings.html', params)


def F480_passChange(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    error = ''
    params = {
        'form': passwordChangeForm(),
        'user': user,
        'error': ''
    }
    if request.method == 'POST':
        form = passwordChangeForm(request.POST)
        if user.password != common_hashing(request.POST['current_password']):
            params['error'] = 'パスワードが正しくありません'
            return render(request, 'user_setting/F480_passChange.html', params)
        if request.POST['new_password'] != request.POST['new_password2']:
            params['error'] = '新しいパスワードが一致しません'
            return render(request, 'user_setting/F480_passChange.html', params)
        if user.password == common_hashing(request.POST['new_password']):
            params['error'] = 'このパスワードは現在使用しています'
            return render(request, 'user_setting/F480_passChange.html', params)
        if form.is_valid():
            print('true')
            user.password = common_hashing(request.POST['new_password'])
            user.update_time = common_current_time()
            user.save()
            return redirect('/F490_passChangeComp')
        else:
            print('false')
            params = {
                'form': passwordChangeForm(request.POST)
            }
            return render(request, 'user_setting/F480_passChange.html', params)
    return render(request, 'user_setting/F480_passChange.html', params)


def F490_passChangeComp(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user,
    }
    return render(request, 'user_setting/F490_passChangeComp.html', params)


def F500_Exit(request, status):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'form': ExitForm(),
        'status': status,
        'user': user,
    }
    if request.method == 'POST':
        if status == 'active':
            reason = request.POST['reason']
            status = 'confirm'
            params = {
                # 'user': user,
                'reason': reason,
                'status': status
            }
            return render(request, 'user_setting/F500_Exit.html', params)
        if status == 'confirm':
            #ユーザーに退会情報を登録する
            user.exit = 1
            user.update_time = common_current_time()
            user.save()
            #exitReasonテーブルに書き込む
            exit_reason = exitReason(
                user = Users.objects.get(id=login_id),
                reason = request.POST['reason'],
                insert_time = common_current_time(),
                update_time = common_current_time(),
            )
            exit_reason.save()
            status = 'complete'
            params = {
                'user': user,
                'status': status
            }
            return render(request, 'user_setting/F500_Exit.html', params)
    return render(request, 'user_setting/F500_Exit.html', params)


def F510_ExitConf(request):
    return render(request, 'user_setting/F510_ExitConf.html')

def F520_ExitComp(request):
    return render(request, 'user_setting/F520_ExitComp.html')

#メールアドレス再設定
def F521_MailChange(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    if request.method == 'POST':
        new_email_address = request.POST['email_address']
        auth_number = round(random() * 1000000)
        mail_change = MailChange(
            user = user,
            old_email_address = user.email_address,
            new_email_address = new_email_address,
            auth_number = auth_number,
            insert_time = common_current_time(),
            update_time = common_current_time(),    
        )
        mail_change.save()
        
        subject = 'メールアドレス変更認証手続き'
        #メールの内容
        context = {
            'auth_number': auth_number,
        }
        message = render_to_string('user_setting/MailChange.txt', context, request)
        #メール送信元
        from_email = settings.DEFAULT_FROM_EMAIL
        #メール送信先
        recipient_list = [new_email_address]
        #Bcc設定
        bcc = [new_email_address]
        #メールの内容を作成・送信
        mail_change_send = EmailMessage(subject, message, from_email, recipient_list, bcc)
        mail_change_send.send()
        return redirect('/F522_MailChangeAuth')
    return render(request, 'user_setting/F521_MailChange.html', params)

#メールアドレス再設定認証
def F522_MailChangeAuth(request):
    if common_logincheck(request, 'login_id') == False:
        return redirect('/F020_userLogin')
    login_id = request.session.get('login_id')
    user = Users.objects.get(id=login_id)
    params = {
        'user': user
    }
    if request.method == 'POST':
        mail_change = MailChange.objects.filter(user=login_id, old_email_address=user.email_address).order_by('-insert_time')[:1]
        auth_number = int(request.POST['auth_number'])
        for m in mail_change:
            #入力された認証コードが一致すれば
            if m.auth_number == auth_number:
                user.email_address = m.new_email_address
                user.save()
                m.del_flg = 1
                m.save()
                return redirect('/F523_MailChangeComp')
            #入力された認証コードが一致しない場合
            else:
                params = {
                    'user': user,
                    'error': '認証コードが違います',
                }
                return render(request, 'user_setting/F522_MailChangeAuth.html', params)
    return render(request, 'user_setting/F522_MailChangeAuth.html', params)

#メールアドレス再設定完了
def F523_MailChangeComp(request):

    return render(request, 'user_setting/F523_MailChangeComp.html')