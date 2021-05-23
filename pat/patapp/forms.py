from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.forms import fields, CharField
from django_filters import widgets

from .models import *

class userForm(forms.ModelForm):
    # hobby = CharField(
    #     widget=widgets.RadioSelect(choices=[(1, "男"), (2, "女"), ]),  # 单选radio
    #     initial=2,
    # )

    class Meta:
        model=UserExtension
        fields=('image','gender','phone','birthday','address','aboutme','like')




