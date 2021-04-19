from django.core.management.base import BaseCommand

from people.models import AppUser, Person

emails = [
    "abc@yahoo.com",
    "def@gmhi.go",
    "me@you.us",
    "baewa@gajo.ge",
    "ageate@iojoij.gejtoij",
]


class Command(BaseCommand):
    help = "Create all permissions"

    def handle(self, *args, **options):

        for idx, email in enumerate(emails):
            try:
                user = AppUser.objects.create_user(email=email, password="password")
                user.is_active = True
            except Exception as e:
                print(e)
                user = AppUser.objects.get(email=email)

            user.save()

            name = f"person {idx}"

            person, _ = Person.objects.get_or_create(user=user)
            person.name = name
            person.save()

            self.stdout.write(self.style.SUCCESS(f"Created {person} successfully"))
