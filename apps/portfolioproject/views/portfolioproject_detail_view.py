from django.shortcuts import get_object_or_404, render
from django.views import View

from apps.portfolioproject.models import Project


class PortfolioProjectDetailView(View):
    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        return render(
            request,
            "portfolioproject/portfolioproject_detail.html",
            {"project": project},
        )
