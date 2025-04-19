from passlib.hash import scrypt

from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import LoginForm, RecoveryForm, RegisterForm
from .models import User


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data["login"]
            password = form.cleaned_data["password"]

            try:
                user = User.objects.get(login=login)
                if scrypt.verify(password, user.password):
                    print(user.type)
                    if user.type == "rh":
                        return redirect("rh:rh")
                    elif user.type == "estoque":
                        return redirect("estoque:estoque")
                    elif user.type == "market":
                        return redirect("market:market")
                    else:
                        return render(
                            request,
                            "user_management/login.html",
                            {"form": form, "error": "Tipo de usuário inválido."},
                        )
                else:
                    return render(
                        request,
                        "user_management/login.html",
                        {"form": form, "error": "Senha inválida."},
                    )
            except User.DoesNotExist:
                return render(
                    request,
                    "user_management/login.html",
                    {"form": form, "error": "Usuário não encontrado."},
                )
    else:
        form = LoginForm()

    return render(request, "user_management/login.html", {"form": form})


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data["login"]
            password = form.cleaned_data["password"]
            name = form.cleaned_data["name"]
            day = form.cleaned_data["day"]
            month = form.cleaned_data["month"]
            year = form.cleaned_data["year"]
            cpf = form.cleaned_data["cpf"]
            email = form.cleaned_data["email"]
            user_type = form.cleaned_data["type"]

            # Verifica se o login ou email já existem
            if User.objects.filter(login=login).exists():
                return JsonResponse({"success": False, "message": "Login já em uso"})
            if User.objects.filter(email=email).exists():
                return JsonResponse({"success": False, "message": "Email já em uso"})

            # Criptografa a senha e formata a data de nascimento
            hashed_password = scrypt.hash(password)
            birthday = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

            try:
                # Cria o usuário no banco de dados
                User.objects.create(
                    login=login,
                    password=hashed_password,
                    name=name,
                    birthday=birthday,
                    cpf=cpf,
                    email=email,
                    type=user_type,
                )
                return JsonResponse(
                    {"success": True, "message": "Usuário registrado com sucesso!"}
                )
            except Exception as e:
                return JsonResponse(
                    {"success": False, "message": f"Ocorreu um erro: {str(e)}"}
                )

    else:
        form = RegisterForm()
        context = {
            "form": form,
        }
        # Não precisa do context.update(dates()), pois o decorador já faz isso
        return render(request, "user_management/register.html", context)


def recovery_view(request):
    if request.method == "POST":
        form = RecoveryForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data["login"]
            try:
                user = User.objects.get(login=login)
                return JsonResponse({"success": True})
            except User.DoesNotExist:
                return JsonResponse(
                    {"success": False, "message": "Usuário não encontrado"}
                )
    else:
        form = RecoveryForm()

    return render(request, "user_management/recovery.html", {"form": form})
