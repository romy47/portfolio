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

    def __str__(self):
        return self.title
    
class ProjectHighlights(models.Model):
    description = models.TextField()
    project = models.ForeignKey('portfolioproject.Project', on_delete = models.PROTECT, related_name = 'project_highlights') 
    url = models.URLField(blank = True, default = '')
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.project}: {self.description}'

class ProjectTool(models.Model):
    programming_tool = models.ForeignKey('programming.ProgrammingTool', on_delete=models.PROTECT, related_name = 'project_tools')
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name = 'project_tools')
    title = models.CharField(max_length=80)
    sub_title = models.CharField(blank=True, default='', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.project}: {self.title}'
