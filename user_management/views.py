from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm
from passlib.hash import scrypt

def login_view(request):
    return render(request, 'user_management/login.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(login=login)
                if scrypt.verify(password, user.password):
                    if user.type == 'rh':
                        return redirect('rh:rh')
                    elif user.type == 'estoque':
                        return redirect('estoque:estoque')
                    elif user.type == 'market':
                        return redirect('market:market')
                    else :
                        return render(request, 'login.html', {
                            'form': form,
                            'error': 'Tipo de usuário inválido.'
                        })
                        

                else:
                    return render(request, 'login.html', {
                        'form': form,
                        'error': 'Senha inválida.'
                    })
            except User.DoesNotExist:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Usuário não encontrado.'
                })
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            day = form.cleaned_data['day']
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            user_type = form.cleaned_data['type']

            if User.objects.filter(login=login).exists():
                return JsonResponse({'success': False, 'message': 'Login já em uso'})
            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'Email já em uso'})

            hashed_password = scrypt.hash(password)
            birthday = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

            try:
                User.objects.create(
                    login=login,
                    password=hashed_password,
                    name=name,
                    birthday=birthday,
                    cpf=cpf,
                    email=email,
                    type=user_type
                )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'message': f'Ocorreu um erro: {str(e)}'})
    current_year = datetime.now().year
    return render(request, 'register.html', {'datetime': datetime, 'current_year': current_year})

def recovery_view(request):
    if request.method == 'POST':
        form = RecoveryForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            try:
                user = User.objects.get(login=login)
                return JsonResponse({'success': True})
            except User.DoesNotExist:
                return JsonResponse({'success': False})
    return render(request, 'recovery.html')
