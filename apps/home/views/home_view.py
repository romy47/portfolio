from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.programming.models import Category
from apps.home.models import Education, Experience, Profile, Publication
from django.db.models import Count

class HomeView(View):
    def get(self, request):
        educations = Education.objects.all().order_by('-ended_at')
        experiences = Experience.objects.all().order_by('-started_at')
        publications = Publication.objects.all().order_by('-year')
        profile = Profile.objects.filter(email='sgomes.cs@gmail.com').first()
        skill_categories = Category.objects.exclude(personal_skills = None)
        return render(
            request,
            'home/home.html',
            {
                'skill_categories': skill_categories,
                'educations': educations,
                'experiences': experiences,
                'publications': publications,
                'profile': profile
            }
        )