'''AUTHS VIEWS'''

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from auths.forms.register_form import RegisterForm
from auths.forms.login_form import LoginForm
from auths.models.my_user import MyUser



class LoginView(View):

    template_name = 'login.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        '''
        POST
        '''

        form = LoginForm(request.POST)
        if form.is_valid():
            user = MyUser.objects.get(email=form.cleaned_data['email'])

            return render(
                request=request,
                template_name='room.html',
                context={
                    'form': form,
                    'user': user,

                }
            )
        
        return render(
            request=request,
            template_name='login.html',
            context={
                'form': form
            }
        )

class RegisterView(View):


    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
            }
        )



    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            MyUser.objects.create(**form.cleaned_data)
        return render(
                request=request,
                template_name=self.template_name,
                context={
                    'form': form
                }
            )
