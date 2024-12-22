from django.contrib import admin
from django.urls import path, include
from gestion import views as gestion_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gestion_views.inicio, name='inicio'),
    path('gestion/', include('gestion.urls')), 
    path('accounts/', include('users.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)