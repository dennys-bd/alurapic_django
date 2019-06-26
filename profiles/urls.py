from django.urls import path
from . import views

urlpatterns = [
    path('', views.indice, name='indice'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('meu_perfil/', views.meu_perfil, name='meu_perfil'),
]
