from django.db import models
class Category(models.Model):
    title = models.CharField(max_length=80)
    image = models.FileField(upload_to ='uploads/')
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProgrammingTool(models.Model):
    title = models.CharField(max_length=80)
    image = models.FileField(upload_to ='uploads/')
    description = models.TextField(blank=True, default='')
    category = models.ForeignKey('programming.Category', on_delete=models.PROTECT, related_name = 'programming_tools')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
