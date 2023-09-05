from django import forms
from auths.models.my_user import MyUser
from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError


class LoginView(forms.ModelForm):

    def clean(self) -> Dict[str,Any]:
            return super().clean()




    def check_auth(self) -> Dict[str, Any]:
        if self.cleaned_data['password'] != self.cleaned_data['password']:
            if self.cleaned_data['email'] != self.cleaned_data['email']:
                raise ValidationError('Пароли не совпадают')
        return self.cleaned_data




    class Meta:
        model = MyUser
        fields = (
            'email',
            'password'
        )