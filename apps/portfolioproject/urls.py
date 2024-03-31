
from django.urls import path
from apps.portfolioproject.views.portfolioproject_view import PortfolioProjectView

urlpatterns = [
    path('', PortfolioProjectView.as_view(), name='project'),
]
