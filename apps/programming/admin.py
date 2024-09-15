from django.contrib import admin
from .models import Category, ProgrammingTool

admin.site.register([Category, ProgrammingTool])
