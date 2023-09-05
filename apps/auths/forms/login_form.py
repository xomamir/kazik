from django import forms
from auths.models.my_user import MyUser
from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=200)
    password = forms.CharField(label='Пароль',min_length=6)
 
    def clean(self) -> Dict[str, Any] :   
        email = self.cleaned_data['email']         
        password = self.cleaned_data['password']         
        if MyUser.objects.filter(email=email, password=password).exists():             
            return self.cleaned_data
        raise ValidationError('не совпадают логин и пароль')