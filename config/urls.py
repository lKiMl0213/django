from django.contrib import admin
from django.urls import path, include
from user_management.views import login_view  # importa a view de login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),   # rota raiz: homepage = tela de login
    path('market/', include('market.urls')),
    path('user_management/', include('user_management.urls')), 
    path('storage/', include('estoque.urls')),
    path('rh/', include('rh_management.urls')),
]
