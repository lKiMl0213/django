from django.db import models
from django.contrib.auth.hashers import make_password


class Address(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True, related_name='addresses')
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Brazil")
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10, blank=True)
    complement = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}, {self.country}, {self.number}, {self.complement}"




class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"
    OTHER = "O", "Other"

class MaritalStatusChoices(models.TextChoices):
    SINGLE = "SINGLE", "Single"
    MARRIED = "MARRIED", "Married"
    DIVORCED = "DIVORCED", "Divorced"
    WIDOWED = "WIDOWED", "Widowed"

class UserType(models.TextChoices):
    HR = "HR", "Human Resources"
    STORAGE = "STORAGE", "Storage"
    MARKET = "MARKET", "Market"
    CLIENT = "CLIENT", "Client"
    ADMIN = "ADMIN", "Admin"

class Benefit(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

class Employee(models.Model):
    photo = models.ImageField(upload_to="photos/", null=True, blank=True, default="photos/default.jpg")
    user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.CLIENT)
    code = models.CharField(max_length=20, unique=True)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    marital_status = models.CharField(max_length=10, choices=MaritalStatusChoices.choices)
    academic_formation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    benefits = models.ManyToManyField(Benefit)
    admission_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')])
    inactive_status = models.CharField(max_length=20, blank=True)
    dismissal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


    @classmethod
    def create_user(cls, login, password, name, birth_date, cpf, email, user_type, code, gender, marital_status, academic_formation, salary, department, position, admission_date, status):
        if not email:
            raise ValueError("Email is required")
        hashed_password = make_password(password)
        return cls(
            login=login,
            password=hashed_password,
            name=name,
            birth_date=birth_date,
            cpf=cpf,
            email=email,
            user_type=user_type,
            code=code,
            gender=gender,
            marital_status=marital_status,
            academic_formation=academic_formation,
            salary=salary,
            department=department,
            position=position,
            admission_date=admission_date,
            status=status,
    )