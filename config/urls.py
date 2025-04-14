from django.contrib import admin
from django.urls import path, include
from user_management.views import login_view  # importa a view de login
from user_management.views import register_view  # importa a view de registro
from user_management.views import recovery_view  # importa a view de recuperação de senha
from estoque.views import estoque_view  # importa a view de estoque
from estoque.views import manage_product  # importa a view de gerenciamento de produtos
from market.views import market_view  # importa a view de mercado 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),   # rota raiz: homepage = tela de login
    path('', register_view, name='register'), # rota raiz: homepage = tela de registro
    path('recovery/', recovery_view, name='recovery'), # rota raiz: homepage = tela de recuperação de senha
    path('user_management/', include('user_management.urls')), 
    path('storage/', include('estoque.urls')),
    path('estoque/', estoque_view, name='estoque'),  # URL para a view de estoque
    path('market/', market_view, name='market'),  # URL para a view de mercado
    path('rh/', include('rh_management.urls')),
]
