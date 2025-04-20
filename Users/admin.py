from django.contrib import admin, messages, make_password
from .models import Benefit, Employee, Address
from .forms import EmployeeForm
import random
import string


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm  # <--- Aqui liga o formulário

    list_display = (
        "name",
        "code",
        "login",
        "email",
        "phone",
        "department",
        "position",
        "salary",
        "status",
        "user_type",
    )
    search_fields = (
        "name",
        "code",
        "login",
        "email",
        "cpf",
        "department",
        "position",
        "user_type",
    )
    list_filter = (
        "department",
        "position",
        "status",
        "gender",
        "marital_status",
        "user_type",
    )
    ordering = ("name",)
    readonly_fields = ("photo",)
    filter_horizontal = ("benefits",)
    actions = ["reset_password"]

    fieldsets = (
        ("Login Info", {
            "fields": ("login", "password", "user_type")
        }),
        ("Personal Info", {
            "fields": ("photo", "name", "cpf", "birth_date", "gender", "marital_status", "phone", "email")
        }),
        ("Job Info", {
            "fields": ("code", "department", "position", "salary", "benefits", "admission_date", "status", "inactive_status", "dismissal_date")
        }),
        ("Address Info", {
            "fields": ("address",)
        }),
        ("Education Info", {
            "fields": ("academic_formation",)
        }),
    )

def reset_password(self, request, queryset):
    for employee in queryset:
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        employee.password = make_password(new_password)
        employee.save()
        self.message_user(
            request,
            f"Senha redefinida para {employee.name}. Nova senha: {new_password}",
            level=messages.INFO,
        )
reset_password.short_description = "Redefinir senha para os selecionados"

@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "number", "city", "state", "zip_code", "country")
    search_fields = ("street", "city", "state", "zip_code", "country")
    list_filter = ("state", "country")
    ordering = ("city", "street")
