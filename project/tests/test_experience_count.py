import pytest
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from portfolio.apps.home.models import Employer, Experience, ExperienceActivity, PersonalSkill
from portfolio.apps.programming.models import Category, ProgrammingTool
    
@pytest.mark.django_db
def test_experience_count():
    """
    Test `experience_count` method of the `PersonalSkill` model.
    
    The ProgrammingTool is parent model which has many `ExperienceActivity` and many `PersonalSkills`.
     
    The PersonalSkill model has an `experience_count` method. This test verifies that the `experience_count` method correctly counts 
    the number of associated `ExperienceActivity` objects through the `ProgrammingTool` model.
    """
    
    # Setup: Create a Category for the ProgrammingTool
    category = Category.objects.create(title="Web Development", image=SimpleUploadedFile("django.png", b"file_content", content_type="image/png"))

    # Setup: Create a ProgrammingTool
    tool = ProgrammingTool.objects.create(title="Django",
        image=SimpleUploadedFile("django.png", b"file_content", content_type="image/png"),
        description="Web framework",
        category=category)
    
    #Create Employer:
    employer = Employer.objects.create(
        name="TechCorp",
        location="New York",
        image=SimpleUploadedFile("logo.png", b"file_content", content_type="image/png"),
        website="https://www.test.com"
    )
    
    #Create Experience:
    experience = Experience.objects.create(
        position="Backend Developer",
        employer=employer,
        short_summary="Worked on backend development using Django.",
        started_at="2023-01-01",
        ended_at="2023-12-31"
    )
    
    # Create the first ExperienceActivity instance
    activity1 = ExperienceActivity.objects.create(
        description="Developed a REST API",
        experience=experience,
        url="https://example.com/api",
        is_featured=True
    )
    activity1.programming_tools.add(tool)
    
    # Create a second ExperienceActivity instance
    activity2 = ExperienceActivity.objects.create(
        description="Developed a React app",
        experience=experience,
        url="https://example.com/app",
        is_featured=True
    )
    activity2.programming_tools.add(tool)
    
    # Create a PersonalSkill associated with the ProgrammingTool
    skill = PersonalSkill.objects.create(
        title="Backend Development",
        programming_tool=tool
    )
    
    # Test: Check the experience_count method
    assert skill.experience_count() == 2  # It should count 2 activities

    # Remove one activity from the ManyToMany relationship and check the count again
    activity1.programming_tools.remove(tool)
    assert skill.experience_count() == 1  # It should count 1 activity