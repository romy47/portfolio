from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from apps.programming.models import Category
from apps.portfolioproject.models import Project
from apps.home.models import Education, Experience, Profile, Publication
from django.db.models import Count

class HomeView(View):
    def get(self, request):
        educations = Education.objects.all().order_by('-ended_at')
        experiences = Experience.objects.all().order_by('-started_at')
        projects = Project.objects.all()
        publications = Publication.objects.all().order_by('-year')
        profile = Profile.objects.first()
        skill_categories = Category.objects.exclude(personal_skills = None)

        # print('Projects Length: ', len(projects))
        return render(
            request,
            'home/home.html',
            {
                'skill_categories': skill_categories,
                'educations': educations,
                'experiences': experiences,
                'publications': publications,
                'profile': profile,
                'projects': projects
            }
        )