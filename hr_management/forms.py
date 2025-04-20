from django import forms
from .models import Employee
from django.contrib.auth.hashers import make_password

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = Employee
        fields = '__all__'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            return make_password(password)
        return self.instance.password
