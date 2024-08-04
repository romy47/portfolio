from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db.models import Q

class Command(BaseCommand):
    def handle(self, *args, **options):
        existing_admin = User.objects.filter(Q(username=settings.SUPERUSER_USERNAME) | Q(email=settings.SUPERUSER_EMAIL)).first()
        if(existing_admin is None):
            superuser = User.objects.create_superuser(
                username=settings.SUPERUSER_USERNAME,
                email=settings.SUPERUSER_EMAIL,
                password=settings.SUPERUSER_PASSWORD)
            superuser.save()
        else:
            print('Super user already exists !')