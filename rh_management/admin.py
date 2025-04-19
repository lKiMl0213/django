from django.contrib import admin

from .models import Benefit, Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
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
    )
    search_fields = ("name", "code", "login", "email", "cpf", "department", "position")
    list_filter = ("department", "position", "status", "gender", "marital_status")
    ordering = ("name",)
    readonly_fields = ("photo",)


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
