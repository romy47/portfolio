from django.contrib import admin
from .models import *

admin.site.register(
    [
        Profile,
        Employer,
        EducationActivity,
        ExperienceActivity,
        Experience,
        EducationalInstitute,
        Education,
        Publication,
        PersonalSkill
    ]
)
