import random
from django.core.management.base import BaseCommand

from voting.models import Point, Vote
from people.models import Person

points = [5, 10, 15]


class Command(BaseCommand):
    help = "Generate random votes"

    def handle(self, *args, **options):
        count = 0
        points = Point.objects.all()
        persons = Person.objects.all()
        contestants = Person.objects.filter(is_contestant=True)

        for voter in persons:

            for contestant in contestants:

                if Vote.objects.filter(voter=voter).count() < 3:

                    for point in points:

                        contestant = random.choice(contestants)

                        vc = {"voter": voter, "contestant": contestant, "point": point}

                        if Vote.objects.filter(**vc).exists():
                            msg = f"{voter} already voted for {contestant}"
                            self.stdout.write(self.style.ERROR(msg))
                        else:
                            vote = Vote.objects.create(**vc)
                            count += 1
                            msg = f"{vote} cast successfully."
                            self.stdout.write(self.style.SUCCESS(msg))

        self.stdout.write(self.style.SUCCESS(f"{count} votes cast."))
