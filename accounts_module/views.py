from audioop import reverse
from django.contrib.auth import login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from django.http import HttpResponse
from accounts_module.forms import sing_up_form, login_form, forgotten_form
from accounts_module.models import User


# Create your views here.

def register_page(request):
    register_form = sing_up_form(request.POST)
    if register_form.is_valid():
        user_fullname = register_form.cleaned_data.get('fullname')
        user_name = register_form.cleaned_data.get('username')
        user_phone = register_form.cleaned_data.get('phone')
        user_email = register_form.cleaned_data.get('email')
        user_password = register_form.cleaned_data.get('password')
        user: bool = User.objects.filter(email__iexact=user_email).exists()
        if user:
            register_form.add_error('email', 'این ایمیل قبلا ثبت نام کرده')
        else:
            new_user = User(
                full_name=user_fullname,
                username=user_name,
                phone_number=user_phone,
                email=user_email,
                email_active_code=get_random_string(48),
                is_active=False,
            )
            new_user.set_password(user_password)
            new_user.save()
            return redirect('home_page')
    context = {
        'register_form': register_form
    }
    return render(request, 'sing_up/Register.html', context)


# def activate_page(request, email_code):
#     user: User = User.objects.filter(email_active_code__iexact=email_code).first()
#     if user is not None:
#         if not user.is_active:
#             user.is_active = True
#             user.email_active_code = get_random_string(48)
#             user.save()
#             return reverse('home_page')
#         else:
#             raise Http404()


class ActivateAccountView(View):
    def get(self, request, email_code):
        user = User.objects.filter(email_active_code__iexact=email_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(48)
                user.save()
                # todo: show success message to user
            else:
                # todo: show your account was activated message to user
                pass

        return redirect('home_page')


def login_page(request):
    Login = login_form(request.POST)
    if Login.is_valid():
        user_email = Login.cleaned_data.get('email')
        user_password = Login.cleaned_data.get('password')
        user: User = User.objects.filter(email__iexact=user_email).first()
        if user is not None:
            if not user.is_active:
                Login.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
            else:
                is_password_correct = user.check_password(user_password)
                if is_password_correct:
                    login(request, user)
                    return redirect('home_page')
                else:
                    Login.add_error('password', 'کلمه عبور یا ایمیل اشتباه می باشد')
    else:
        Login.add_error('email', 'حساب کاربری شما فعال نشده است')

    context = {
        'login_form': Login,
    }
    return render(request, 'sing_in/Login.html', context)


def forgot_password_page(request):
    forgot_page = forgotten_form(request.POST)
    if forgot_page.is_valid():
        user_email = forgot_page.cleaned_data.get('email')
        user: User = User.objects.filter(email__iexact=user_email).first()
        if user is not None:
            return redirect('home_page')
    context = {'forgot_form': forgot_page}
    return render(request, 'forgot_password/forgot_page.html', context)


def logout_page(request):
    logout(request)
    return redirect('Login')
