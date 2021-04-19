from django.db import IntegrityError
from django.core.management.base import BaseCommand

from people.models import AppUser


class Command(BaseCommand):
    help = 'Create a user optionally passing an email and password'

    def add_arguments(self, parser):
        parser.add_argument('-is_super', type=bool)
        parser.add_argument('-email', type=str)
        parser.add_argument('-password', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Create user'))
        email = options['email']
        is_super = options['is_super']
        password = options['password']

        if not email:
            self.stdout.write(self.style.ERROR('Please provide an email address'))
            return

        if not password:
            self.stdout.write(self.style.ERROR('Please provide a password'))
            return

        try:
            su = AppUser.objects.create_user(email=email, password=password)
            su.is_active = True

            if is_super:
                su.is_admin = True
                su.is_superuser = True
            su.save()
            self.stdout.write(self.style.SUCCESS(f'User {email} created successfully'))
        except IntegrityError:
            self.stdout.write(self.style.ERROR(f'User {email} already exists'))
