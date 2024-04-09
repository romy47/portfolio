from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    short_bio = models.CharField(max_length=80)
    about_me = models.TextField()
    image = models.FileField(upload_to = 'uploads/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Employer(models.Model):
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    image = models.FileField(upload_to ='uploads/')
    website = models.URLField(blank = True, default = '')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class EducationActivity(models.Model):
    description = models.TextField()
    education = models.ForeignKey('home.Education', on_delete = models.PROTECT, related_name = 'education_activities') 
    url = models.URLField(blank = True, default = '')
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class ExperienceActivity(models.Model):
    description = models.TextField()
    experience = models.ForeignKey('home.Experience', on_delete = models.PROTECT, related_name = 'experience_activities') 
    programming_tools = models.ManyToManyField('programming.ProgrammingTool', related_name = 'experience_activities', blank=True) 
    url = models.URLField(blank = True, default = '')
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.experience}: {self.description[:50] if len(self.description)>49 else self.description[:len(self.description)]}' 
    
class Experience(models.Model):
    position = models.CharField(max_length=80)
    employer = models.ForeignKey(Employer, on_delete = models.PROTECT, related_name = 'experiences')
    short_summary = models.TextField()
    started_at = models.DateField()
    ended_at = models.DateField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.position 

class EducationalInstitute(models.Model):
    name = models.CharField(max_length=80)
    image = models.FileField(upload_to ='uploads/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=80)
    specialization = models.CharField(max_length=80, blank=True, default='')
    institute = models.ForeignKey(EducationalInstitute, on_delete = models.PROTECT, related_name = 'institutes')
    short_summary = models.TextField()
    started_at = models.DateField()
    ended_at = models.DateField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.degree

class Publication(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(blank = True, null=True)
    description = models.TextField(blank = True, default = '')
    url = models.URLField(blank = True, default = '')
    is_featured = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return (self.title[:50]+'...') if len(self.title)>49 else self.title[:len(self.title)] 