from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.portfolioproject.models import Project

class PortfolioProjectView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(
            request,
            'portfolioproject/portfolioproject.html',
                {
                    'projects': projects
                }
            )