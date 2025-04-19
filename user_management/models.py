from django.db import models


class User(models.Model):
    class UserType(models.TextChoices):
        HR = "HR", "Human Resources"
        STORAGE = "STORAGE", "Storage"
        MARKET = "MARKET", "Market"

    login = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    cpf = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    type = models.CharField(
        max_length=10, choices=UserType.choices, null=False, blank=False
    )

    def __str__(self):
        return f"{self.login} ({self.name})"
