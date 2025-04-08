from django import forms

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField()
    day = forms.IntegerField(min_value=1, max_value=31)
    month = forms.IntegerField(min_value=1, max_value=12)
    year = forms.IntegerField(min_value=1900, max_value=2100)
    cpf = forms.CharField()
    email = forms.EmailField()
    type = forms.CharField()

class RecoveryForm(forms.Form):
    login = forms.CharField()
