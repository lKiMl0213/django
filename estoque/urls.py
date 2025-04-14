from django.urls import path
from .views import estoque_view  # importa a view de estoque

app_name = 'estoque'

urlpatterns = [
    path('estoque/', estoque_view, name='estoque'),  # URL para a view de estoque

]
