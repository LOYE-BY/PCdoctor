# coding=utf-8
from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=128, help_text="Please enter the category name.")
    # views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    # likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    # slug = forms.CharField(widget = forms.HiddenInput(), required = False)

    class Meta:
        """model建立表单和模型类的关联，fields里包含表单显示出来的字段"""
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    """docstring for PageForm"""
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # model简历表单和模型类的关联，排除exclude里包含的字段，其它字段显示
        model = Page
        exclude = ('category',)
    '''fields = ('title', 'url', 'views')'''


class UserForm(forms.ModelForm):
    """创建用户表单"""
    passwd = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
