from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('moveis/<int:id>/', views.detalhe, name='detalhe'),
]