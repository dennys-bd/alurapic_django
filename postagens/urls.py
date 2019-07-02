from django.urls import path, include
from . import views

app_name = 'postagens'
urlpatterns = [
    path('nova/', views.nova, name='nova')
]
