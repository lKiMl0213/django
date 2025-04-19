from django.db import models


class Employee(models.Model):
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    code = models.CharField(max_length=20, unique=True)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=9)
    academic_formation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    benefits = models.ManyToManyField(to="rh_management.Benefit")

    admission_date = models.DateField()
    status = models.CharField(max_length=20)
    inactive_status = models.CharField(max_length=20, blank=True)
    date_of_dismissal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Benefit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
