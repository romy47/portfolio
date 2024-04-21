
from django.urls import path
from apps.portfolioproject.views.portfolioproject_view import PortfolioProjectView
from apps.portfolioproject.views.portfolioproject_detail_view import PortfolioProjectDetailView

urlpatterns = [
    path('', PortfolioProjectView.as_view(), name='project'),
    path('<int:project_id>', PortfolioProjectDetailView.as_view(), name='project_detail'),
]
