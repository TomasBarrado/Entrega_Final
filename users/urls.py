from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.registro, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', views.perfil, name='perfil'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('agregar-imagen/', views.agregar_imagen, name='AgregarImagen'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)