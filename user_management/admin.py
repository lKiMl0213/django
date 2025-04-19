from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("login", "name", "email", "type", "birthday")
    list_filter = ("type", "birthday")
    search_fields = ("login", "name", "email", "cpf")
    ordering = ("name",)
