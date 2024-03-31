from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('apps.blog.urls')),
    path('projects/', include('apps.portfolioproject.urls')),
    path('', include('apps.home.urls')),
]
