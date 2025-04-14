from django.contrib import admin
from django.urls import path, include
from user_management.views import login_view, register_view, recovery_view
from estoque.views import estoque_view, manage_product
from market.views import market_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Telas de autenticação no nível raiz
    path('', login_view, name='login'),  # homepage = login
    path('register/', register_view, name='register'),
    path('recovery/', recovery_view, name='recovery'),

    # Apps
    path('user_management/', include('user_management.urls')), 
    path('storage/', estoque_view, name='estoque'),
    path('market/', market_view, name='market'),
    path('rh/', include('rh_management.urls')),
]
