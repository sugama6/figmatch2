from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import CharField, Model, IntegerField

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='名前')
    password = models.CharField(max_length=70, verbose_name='パスワード')
    user_image = models.ImageField(verbose_name='プロフィール画像')
    lock_flg = models.BooleanField(default=0, verbose_name='ロック')
    lock_count = models.IntegerField(default=0, verbose_name='ロック回数')
    email_address = models.EmailField(unique=True, verbose_name='メールアドレス')
    telephone_number = models.IntegerField(null=True, verbose_name='電話番号')
    acount_name = models.CharField(unique=True, max_length=30, verbose_name='アカウント名')
    board_release = models.BooleanField(default=0, verbose_name='掲示板公開')
    age = models.CharField(max_length=99, null=True, verbose_name='年齢')
    age_flg = models.BooleanField(default=0, verbose_name='年齢公開フラグ')
    sex = models.CharField(max_length=3, null=True, verbose_name='性別')
    sex_flg = models.BooleanField(default=0, verbose_name='性別公開フラグ')
    introduction = models.CharField(max_length=500, null=True, verbose_name='自己紹介')
    category = ArrayField(
        base_field=IntegerField(),
        size=50,
        null=True,
        max_length=(50 * 110),
        verbose_name='カテゴリー'
    )
    exit = models.BooleanField(default=0, verbose_name='退会状況')
    suspension = models.BooleanField(default=0, verbose_name='アカウント停止')
    gold_point = models.IntegerField(default=0, verbose_name='保有ゴールドポイント')
    silver = models.IntegerField(default=0, verbose_name='保有シルバーポイント')
    gift = models.CharField(max_length=100, null=True, verbose_name='所有ギフト')
    nick_name = models.CharField(max_length=20, null=True, verbose_name='ニックネーム')
    identification_status = models.BooleanField(default=0, verbose_name='本人確認ステータス')
    identification_image = models.ImageField(null=True, verbose_name='本人確認画像')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class Board(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    board_title = models.CharField(max_length=30, verbose_name='タイトル')
    category1 = models.IntegerField(verbose_name='カテゴリー1')
    category2 = models.IntegerField(null=True, verbose_name='カテゴリー2')
    category3 = models.IntegerField(null=True, verbose_name='カテゴリー3')
    participation_conditions = models.CharField(max_length=100, verbose_name='参加条件')
    thumbnail = models.ImageField(verbose_name='サムネイル')
    wallpaper = models.CharField(max_length=60, null=True, verbose_name='壁紙')
    introduction = models.CharField(max_length=500, verbose_name='掲示板紹介文')
    comment_count = models.IntegerField(default=0, verbose_name='コメント数')
    good_count = models.IntegerField(default=0, verbose_name='いいね数')
    release_flg = models.BooleanField(verbose_name='公開フラグ')
    del_flg = models.BooleanField(verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')

class FIGmatch(models.Model):
    figmatch_name = models.CharField(max_length=30, verbose_name='FIGmatch名')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    thumbnail = models.ImageField(verbose_name='サムネイル')
    category = ArrayField(
        base_field=IntegerField(),
        size=50,
        null=True,
        max_length=(50 * 110),
        verbose_name='カテゴリー'
    )
    figmatch_date = models.DateTimeField(verbose_name='開催日時')
    recruitment_conditions = models.CharField(max_length=100, verbose_name='募集条件')
    recruitment_person = models.IntegerField(verbose_name='募集人数')
    join_person = models.IntegerField(verbose_name='参加者人数')
    greeting = models.CharField(max_length=200, verbose_name='主催者からの挨拶')
    overview = models.CharField(max_length=1000, verbose_name='概要')
    place = models.CharField(max_length=100, verbose_name='開催場所')
    application_status = models.IntegerField(default=0, verbose_name='申請状況')
    price = models.CharField(max_length=30, verbose_name='料金')
    release_flg = models.BooleanField(default=0, verbose_name='公開フラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class Notification(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    read = models.BooleanField(default=0, verbose_name='既読')
    message = models.CharField(max_length=1000, verbose_name='メッセージ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class BoardGood(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='掲示板ID')
    good_flg = models.BooleanField(verbose_name='いいねフラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class BoardComment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='掲示板ID')
    message = models.CharField(max_length=1000, verbose_name='メッセージ')
    good_count = models.IntegerField(default=0, verbose_name='いいね数')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class BoardCommentGood(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    board_comment = models.ForeignKey(BoardComment, on_delete=models.CASCADE, verbose_name='掲示板コメントID')
    good_flg = models.BooleanField(verbose_name='いいねフラグ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class BoardViewerComment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='ユーザーID')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='掲示板ID')
    message = models.CharField(max_length=1000, verbose_name='メッセージ')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')


class Report(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='通報ユーザーID')
    report_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='report_user', verbose_name='通報されたユーザーID')
    message = models.CharField(max_length=1000, verbose_name='メッセージ')
    Evidence_photo = models.ImageField(verbose_name='証拠写真')
    Confirmation_status = models.BooleanField(default=0, verbose_name='確認状況')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')

class FIGmatchJoin(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='通報ユーザーID')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name='掲示板ID')
    message = models.CharField(max_length=1000, verbose_name='参加者ユーザーID')
    join_status = models.BooleanField(verbose_name='参加状況')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')

class adminUser(models.Model):
    user_name = models.CharField(max_length=30, verbose_name='ユーザー名')
    password = models.CharField(max_length=20, verbose_name='パスワード')
    lock_flg = models.BooleanField(verbose_name='ロック')
    lock_count = models.IntegerField(verbose_name='ロック回数')
    del_flg = models.BooleanField(default=0, verbose_name='削除フラグ')
    insert_time = models.DateTimeField(verbose_name='登録日時')
    update_time = models.DateTimeField(verbose_name='更新日時')

