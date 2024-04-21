from django.db import models
from ckeditor.fields import RichTextField
class Project(models.Model):
    title = models.CharField(max_length=80)
    sub_title = models.CharField(blank=True, default='', max_length=120)
    image = models.FileField(upload_to ='uploads/')
    description = RichTextField(blank=True, default='')
    programming_tools = models.ManyToManyField('programming.ProgrammingTool', through='portfolioproject.ProjectTool')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProjectTool(models.Model):
    programming_tool = models.ForeignKey('programming.ProgrammingTool', on_delete=models.PROTECT, related_name = 'project_tools')
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name = 'project_tools')
    title = models.CharField(max_length=80)
    sub_title = models.CharField(blank=True, default='', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
