from django.urls import path
from . import views

app_name = 'rh_management'  # deixar igual ao nome real do app

urlpatterns = [
    path('', views.home_view, name='home'),  # agora você pode usar 'rh_management:home'
]
