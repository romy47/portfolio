from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.programming.models import Category
from apps.home.models import Education, Experience

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        educations = Education.objects.all()
        experiences = Experience.objects.all()
        return render(
            request,
            'home/home.html',
            {
                'categories': categories,
                'educations': educations,
                'experiences': experiences
            }
        )