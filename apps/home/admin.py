from django.contrib import admin

from .models import Profile, Employer, EducationActivity, \
                    ExperienceActivity, Experience, EducationalInstitute, \
                    Education, Publication, PersonalSkill

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
