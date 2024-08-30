from django import forms


class Profile(forms.Form):
    profile = forms.FileField()