from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog')),
    path('', include('materials.urls', namespace='materials')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
