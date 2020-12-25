from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from figmatch import settings
from app.models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import math
import sys
import os
import hashlib
import base64
import random
import string
import csv

#ログアウト
def common_logout(request):
  # root = request.POST['root']
  to = request.POST['to']
  request.session.clear()
  # request.session[root] = ""
  return redirect(to)


#メール送信
def common_send_email(request, email):
    #リンク用トークン
    token = get_random_chars()
    try:
        testuser = testUser.objects.get(email_address=email)
        subject = 'ユーザーID確認・パスワード再設定手続きのご確認'
        context = {
          'user': testuser,
          'token': token,
        }
        message = render_to_string('test/mail.txt', context, request)
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        bcc = [email]
        password_reset_mail = EmailMessage(subject, message, from_email, recipient_list, bcc)
        password_reset_mail.send()
    except:
        pass

#ユーザーセッション作成
def create_user_session(request, user_id):
    request.session.clear()
    request.session['login_id'] = user_id

#管理者ログインセッション作成
def create_admin_session(request, user_id):
    request.session.clear()
    request.session['admin_login_id'] = user_id

#ログアウト機能
def common_logout(request):
    to = request.POST['to']
    request.session.clear()
    return redirect(to)
  
#ログインチェック機能
def common_logincheck(request, keyname):
    keyjudge = keyname in request.session
    if keyjudge == False:
        request.session[keyname] = ""
    if request.session[keyname] == "":
        return False
    return True

#ランダムトークン作成
def get_random_chars(char_num=30):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(char_num)])

#文字のハッシュ化(sha256)
def common_hashing(str):
    h = hashlib.sha256(str.encode('utf-8')).hexdigest()
    return h

#現在時刻取得
def common_current_time():
    now = timezone.now()
    return now

#2ヶ月後の時刻取得
def common_add_twomonth():
    time = timezone.now() + relativedelta(month=2)
    return time


#pdfアップロード機能
def common_uploaded_pdf(file, name):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file.name + "\n")
    file_name = file.name
    extension = str(file_name).split('.')[-1]
    hs_filename = '%s.%s' % (hashlib.md5(file_name.encode()).hexdigest(), extension)
    os.makedirs('app/static' + name, exist_ok=True)
    file_path = 'app/static' + name  +  hs_filename
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            print(destination.write(chunk))
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")          
            return '/static' + name + hs_filename

#ページネーション機能
def common_PageNator(obj,num,page):
    p = Paginator(obj, num)
    max = math.ceil(p.count / num)
    if page == 1:
        pagePrev = 1
    else:
        pagePrev = page - 1
    if page == max:
        pageNext = page
    else:
        pageNext = page + 1
    # print(type(p.get_page(page)))
    result = {
        "queryset": p.get_page(page),
        "page": page,
        "prev": pagePrev,
        "next": pageNext
      }
    return result

#CSV出力
def text_csv_converter(file_dir, query, fields):
  #テキストファイルの初期化
  with open(file_dir, mode='w') as f:
      f.write('')   
  with open(file_dir, "w", encoding='utf_8') as open_file:
      for f in range(0, len(fields)):
          # open_file.write('ID&test1&test2&test3&test4&test5&test6&')
          open_file.write(fields[f] + '&')
      open_file.write('\n')
      for q in query:
          open_file.write(str(q) + '&')
          # open_file.write(str(q.test1) + '&')
          # open_file.write(str(q.test2) + '&')
          # open_file.write(str(q.test3) + '&')
          # open_file.write(str(q.test4) + '&')
          # open_file.write(str(q.test5) + '&')
          # open_file.write(str(q.test6) + '&')
          open_file.write('\n')     
  file_csv = file_dir.replace("txt", "csv")
  with open(file_dir, "r", encoding='utf_8_sig') as rf:
      with open(file_csv, "w", encoding='utf_8_sig') as wf:
          readfile = rf.readlines()                
          print(readfile)
          for read_text in readfile:
              read_text = read_text.split('&')
              writer = csv.writer(wf, delimiter=',')
              writer.writerow(read_text)

def getfnames(models):
        print('go')
        meta_fields = models._meta.get_fields()
        print(meta_fields)  # ※1
        ret = list()
        for i, meta_field in enumerate(meta_fields):
            if i > 0:
                ret.append(meta_field.name)
        print(type(len(ret)))   # ※2)
        return ret