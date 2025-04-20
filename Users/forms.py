from django import forms
from django.contrib.auth.hashers import make_password
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"  # Pode ser todos os campos mesmo

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password and not password.startswith('pbkdf2_'):  # Garante que não recripte uma senha já salva
            return make_password(password)
        return password
