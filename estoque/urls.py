from django.urls import path
from .views import estoque_view, manage_product  # <-- garantir que manage_product esteja importado

app_name = 'estoque'

urlpatterns = [
    path('manage/', manage_product, name='manage_product'),
]
