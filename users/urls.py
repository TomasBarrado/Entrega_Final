from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.registro, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', views.perfil, name='perfil'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
]
