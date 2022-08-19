import os

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from dotenv import load_dotenv

load_dotenv()

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = os.getenv('DJANGO_USERNAME_ADMIN')
            password = os.getenv('DJANGO_PASSWORD_ADMIN')
            email = os.getenv('DJANGO_EMAIL_ADMIN')
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
            )
            print('Admin user initialized')
        else:
            print('Admin user has already been initialized')

