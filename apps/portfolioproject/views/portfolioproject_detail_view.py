from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class PortfolioProjectDetailView(View):
    def get(self, request, project_id):
        return render(request, template_name = 'portfolioproject/portfolioproject_detail.html')