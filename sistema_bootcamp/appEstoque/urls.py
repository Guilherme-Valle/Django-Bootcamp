from django.urls import path
from .import views

app_name = 'appEstoque'

# http://127.0.0.1:8000/ControleEstoque/
urlpatterns = [
    path('', views.home, name='home'),
    path('Cadastro', views.cadastro, name='cadastro'),
    path('Lista', views.lista, name='lista'),
]