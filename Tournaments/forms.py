from django import forms


class Profile(forms.Form):
    Image = forms.ImageField()
