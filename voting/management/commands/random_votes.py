import random
from django.core.management.base import BaseCommand

from voting.models import Point
from people.models import Person, PersonVote


points = [5, 10, 15]


class Command(BaseCommand):
    help = "Generate random votes"

    def handle(self, *args, **options):
        points = Point.objects.all()
        persons = Person.objects.all()
        contestants = Person.objects.filter(is_contestant=True)

        for _ in range(80):
            point = random.choice(points)
            voter = random.choice(persons)
            voted_for = random.choice(contestants)

            vote = PersonVote.objects.create(
                voter=voter, vote=point, voted_for=voted_for
            )
            self.stdout.write(self.style.SUCCESS(f"{vote} cast successfully."))
