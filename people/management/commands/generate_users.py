import random
from django.core.management.base import BaseCommand
from faker import Faker

from people.models import AppUser, Person

emails = [
    "abc@yahoo.com",
    "def@gmhi.go",
    "me@you.us",
    "baewa@gajo.ge",
    "ageate@iojoij.gejtoij",
    "aeer@ojo.go",
    "toij@oiioo.gg",
]

fake = Faker()
class Command(BaseCommand):
    help = "Generate random users"

    def handle(self, *args, **options):

        for user in range(80):
            email=fake.email()
            name = fake.name()

            try:
                user = AppUser.objects.create_user(email=email, password="password")
                user.is_active = True
            except Exception as e:
                print(e)
                user = AppUser.objects.get(email=email)

            user.save()

            person, _ = Person.objects.get_or_create(user=user)
            person.name = name
            person.save()

            self.stdout.write(self.style.SUCCESS(f"Created {person} successfully"))

        # mark 10 persons as contestants
        persons = Person.objects.all()
        for i in range(10):
            p = random.choice(persons)
            p.is_contestant = True
            p.save(update_fields=['is_contestant'])
