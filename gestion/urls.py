from django.urls import path
from . import views

urlpatterns = [
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('mascotas/editar/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:pk>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),
    path('veterinarios/', views.lista_veterinarios, name='lista_veterinarios'),
    path('buscar-veterinario/', views.buscar_veterinario, name='buscar_veterinario'),
    path('', views.inicio, name='inicio'),
]
