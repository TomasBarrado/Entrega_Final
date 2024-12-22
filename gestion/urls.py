from django.urls import path
from . import views
from gestion import views as gestion_views


urlpatterns = [
    
    path('veterinarios/', gestion_views.ListaVeterinariosView.as_view(), name='lista_veterinarios'),
    path('veterinarios/editar/<int:pk>/', gestion_views.EditarVeterinarioView.as_view(), name='editar_veterinario'),
    path('veterinarios/eliminar/<int:pk>/', gestion_views.EliminarVeterinarioView.as_view(), name='eliminar_veterinario'),
    path('usuarios/', gestion_views.ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('usuarios/editar/<int:pk>/', gestion_views.EditarUsuarioView.as_view(), name='editar_usuario'),
    path('servicios/', gestion_views.ListaServiciosView.as_view(), name='lista_servicios'),
    path('servicios/editar/<int:pk>/', gestion_views.EditarServicioView.as_view(), name='editar_servicio'),
    path('veterinarios/agregar/', views.agregar_veterinario, name='agregar_veterinario'),
    path('servicios/eliminar/<int:pk>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('mascotas/dueños/', gestion_views.MascotasPorUsuarioView.as_view(), name='mascotas_por_usuario'),
]


urlpatterns += [
    path('', gestion_views.inicio, name='inicio'),
    path('servicios/', gestion_views.ListaServiciosView.as_view(), name='lista_servicios'),
    path('veterinarios/', gestion_views.lista_veterinarios, name='lista_veterinarios'),
    path('mascotas/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('buscar-veterinario/', gestion_views.buscar_veterinario, name='buscar_veterinario'),
    path('about/', views.about, name='about'),
    
    
    path('mascotas/', views.ListaMascotasView.as_view(), name='lista_mascotas'),
    path('mascotas/editar/<int:pk>/', views.EditarMascotaView.as_view(), name='editar_mascota'),
    path('mascotas/eliminar/<int:pk>/', views.EliminarMascotaView.as_view(), name='eliminar_mascota'),
]
