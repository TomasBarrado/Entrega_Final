from django.contrib import admin
from django.urls import path, include
from gestion import views as gestion_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestion_views.inicio, name='inicio'),
    path('gestion/', include('gestion.urls')), 
    path('accounts/', include('users.urls')), 
]

