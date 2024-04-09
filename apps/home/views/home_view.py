from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.programming.models import Category
from apps.home.models import Education, Experience, Profile, Publication

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        educations = Education.objects.all().order_by('-ended_at')
        experiences = Experience.objects.all().order_by('-started_at')
        publications = Publication.objects.all().order_by('-year')
        profile = Profile.objects.filter(email='sgomes.cs@gmail.com').first()
        return render(
            request,
            'home/home.html',
            {
                'categories': categories,
                'educations': educations,
                'experiences': experiences,
                'publications': publications,
                'profile': profile
            }
        )