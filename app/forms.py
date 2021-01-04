from django import forms
from app.models import *

SEX_CHOICE = (
    ('男性','男性'),
    ('女性','女性'),
    ('どちらも','どちらも'),
)

RELEASE_CHOICE = (
    (True, '公開'),
    (False, '非公開')
)
CATEGORY_CHOICE = (
    ('時事ネタ','時事ネタ'),
    ('豆知識','豆知識'),
    ('お笑い','お笑い'),
    ('科学','科学'),
    ('アダルト','アダルト'),
    ('秘密の話','秘密の話'),
    ('悩み相談','悩み相談'),
    ('恋愛','恋愛'),
    ('自然','自然'),
    ('感動','感動'),
    ('怖い・不思議','怖い・不思議'),
    ('旅行','旅行'),
    ('ドラマ・映画・アニメ','ドラマ・映画・アニメ'),
    ('グルメ','グルメ'),
    ('ゲーム','ゲーム'),
    ('ショッピング','ショッピング'),
    ('スポーツ','スポーツ'),
)

#初回会員登録フォーム
class InitialRegistrationForm(forms.Form):
    nick_name = forms.CharField(max_length=20)
    acount_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20 ,widget=forms.PasswordInput(attrs={'pattern': '(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{6,}'}))
    password2 = forms.CharField(max_length=20 ,widget=forms.PasswordInput(attrs={'pattern': '(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{6,}'}))
    email_address = forms.EmailField(max_length=50)

#ユーザープロフィール編集フォーム
class userProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(userProfileForm, self).__init__(*args, **kwargs)
        self.fields['acount_name'] = forms.CharField(max_length=30, required=False)
        self.fields['nick_name'] = forms.CharField(max_length=20, required=False)
        self.fields['sex'] = forms.ChoiceField(choices=SEX_CHOICE, widget=forms.Select(), required=False)
        self.fields['sex_flg'] = forms.ChoiceField(choices=RELEASE_CHOICE, widget=forms.CheckboxInput(), required=False)
        self.fields['age'] = forms.IntegerField(required=False)
        self.fields['age_flg'] = forms.ChoiceField(choices=RELEASE_CHOICE, widget=forms.CheckboxInput(), required=False)
        self.fields['category'] = forms.MultipleChoiceField(choices=CATEGORY_CHOICE, widget=forms.CheckboxSelectMultiple(), required=False)
        self.fields['introduction'] = forms.CharField(max_length=500, widget=forms.Textarea(), required=False)
    class Meta:
        model = Users
        fields = (
            'acount_name', 'nick_name', 'sex' ,'sex_flg', 'age', 'age_flg', 'category', 'introduction',
        )

#パスワードチェンジフォーム
class passwordChangeForm(forms.Form):
    current_password = forms.CharField(max_length=20 ,widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=20 ,widget=forms.PasswordInput(attrs={'pattern': '(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{6,}'}))
    new_password2 = forms.CharField(max_length=20 ,widget=forms.PasswordInput(attrs={'pattern': '(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]{6,}'}))

#退会フォーム
class ExitForm(forms.Form):
    reason = forms.CharField(max_length=500, widget=forms.Textarea())

#掲示板作成フォーム
class CreateBoardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateBoardForm, self).__init__(*args, **kwargs)
        self.fields['category1'] = forms.ChoiceField(choices=CATEGORY_CHOICE, widget=forms.Select())
        self.fields['introduction'] = forms.CharField(max_length=500, widget=forms.Textarea())
        self.fields['release_flg'] = forms.ChoiceField(choices=RELEASE_CHOICE, widget=forms.Select(), required=False)
    class Meta:
        model = Board
        fields = (
            'board_title', 'category1', 'introduction',\
            'participation_conditions', 'release_flg'
        )