from .models import Video
from django import forms
from django.db import models
from captcha.fields import CaptchaField


class Video_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=Video
        fields=("caption","video")
        ordering = ['-date',]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

