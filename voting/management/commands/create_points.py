from django.core.management.base import BaseCommand

from voting.models import Point


points = [5, 10, 15]


class Command(BaseCommand):
    help = "Create all permissions"

    def handle(self, *args, **options):

        for p in points:
            v, created = Point.objects.get_or_create(points=p)
            if created:
                self.stdout.write(self.style.SUCCESS(f"{v} created successfully"))
            else:
                self.stdout.write(self.style.SUCCESS(f"{v} already exists"))
