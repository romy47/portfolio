from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, template_name = 'home/home.html')