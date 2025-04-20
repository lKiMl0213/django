from django.urls import path
from .views import storage_view, manage_product  # <-- garantir que manage_product esteja importado

app_name = 'storage'

urlpatterns = [
    path('manage/', manage_product, name='manage_product'),
]
