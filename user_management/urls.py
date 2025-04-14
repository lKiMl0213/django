from django.urls import path
from .views import login_view, register_view, recovery_view

app_name = 'user_management'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('recovery/', recovery_view, name='recovery'),
]
