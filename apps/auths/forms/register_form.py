from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from auths.models.my_user import MyUser


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=200)
    nickname = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Пароль',min_length=6)
    password2 = forms.CharField(label='Повторите Пароль',min_length=6)


    def clean(self) -> Dict[str,Any]:
        return super().clean()


    def clean_email(self):
        data: str = self.cleaned_data['email']
        if '@gmail' in data:
            raise ValidationError('фу, gei!')
        return data


    def clean_password2(self) -> Dict[str, Any]:
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError('Пароли не совпадают')
        return self.cleaned_data