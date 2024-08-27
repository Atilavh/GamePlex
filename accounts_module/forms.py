from django import forms
from django.core.exceptions import ValidationError


class sing_up_form(forms.Form):
    fullname = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'color': 'white',
                'placeholder': 'نام خود را وارد کنید',
                'class': 'single-input mb-6'
            }))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "نام کاربری خود را وارد کنید",
                'class': 'single-input mb-6'
            }))
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "شماره موبایل خود را وارد کنید",
                'class': 'single-input mb-6'
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': "ایمیل خود را وارد کنید",
                'class': 'single-input mb-6'
            }))
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "کلمه عبور خود را وارد کنید",
                'class': 'single-input mb-6'
            }))

    # def clean_confirm_password(self):
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if password == confirm_password:
    #         return confirm_password
    #
    #     raise ValidationError('کلمه عبور و تکرار کلمه عبور باهم مغایرت دارد')


class login_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
            'class': 'single-input mb-6',
        }))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'کلمه عبور خود را وارد کنید',
            'class': 'single-input mb-6',
        }))
