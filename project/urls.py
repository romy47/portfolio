from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('apps.blog.urls')),
    path('projects/', include('apps.portfolioproject.urls')),
    path('', include('apps.home.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
