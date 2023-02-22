from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('sucursales/', views.sucursales, name="Sucursales"),
    path('productos/', views.productos, name="Productos"),
    path('consultas/', views.consultas, name="Consultas"),
    path('',views.busqueda_productos, name="busqueda_productos"),
    path('buscar/',views.buscar),
]