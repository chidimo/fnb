from django.core.management.base import BaseCommand


all_permissions = []


class Command(BaseCommand):
    help = 'Create all permissions'

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS(f'Created permissions'))
