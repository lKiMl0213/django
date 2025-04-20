from django.contrib import admin
from django.urls import path, include
from user_management.views import login_view, register_view, recovery_view
from storage.views import storage_view
from market.views import market_view
from hr_management.views import hr_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Telas de autenticação no nível raiz
    path('', login_view, name='login'),  # homepage = login
    path('register/', register_view, name='register'),
    path('recovery/', recovery_view, name='recovery'),

    # Apps
    path('user_management/', include('user_management.urls')), 
    path('storage/', storage_view, name='storage'),  # URL para a view de estoque
    path('storage/', include('storage.urls')),  # URL para a view de estoque
    path('market/', market_view, name='market'),
    path('hr/', include('hr_management.urls')),
]