
from django.urls import path
from apps.blog.views.blogs_view import BlogsView

urlpatterns = [
    path('', BlogsView.as_view(), name='blogs'),
]
