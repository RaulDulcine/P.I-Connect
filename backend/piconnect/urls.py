from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

admin.site.site_header = "PI Connect"
admin.site.site_title  = "PI Connect Admin"
admin.site.index_title = "Painel de Administração"

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Serve arquivos de upload em desenvolvimento (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
