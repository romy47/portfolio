from django.contrib import admin
from .models import Project, ProjectTool, ProjectHighlights

admin.site.register([Project, ProjectTool, ProjectHighlights])
