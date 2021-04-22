import random
from django.core.management.base import BaseCommand

from voting.models import Point, Vote
from people.models import AppUser, Person

points = [5, 10, 15]

people = [
    ("vanessarestscene@gmail.com", "Nessa"),
    ("Barnabas.emordi@yahoo.com", "Barnabas “Barny” Emordi"),
    ("chatwithdexter@yahoo.com", "Nwigbo Ogechukwu A"),
    ("mizzbozz19@yahoo.com", "Menah aka modern Day Mary Jane"),
    ("chrisgina14@gmail.com", "GINA"),
    ("blazem352@gmail.com", "Nelly Sylva"),
    ("anne4mii@gmail.com", "Annabel"),
    ("mreze990@gmail.com", "Eze Collins Ejike"),
    ("lifeofikay@gmail.com", "iKAY"),
    ("oduegwuifeoma@gmail.com", "Ifeoma Oduegwu"),
    ("sikadseeker@yahoo.com", "Seeker"),
    ("qfire995@gmail.com", "Fionadafire"),
    ("oriafohprecious@gmail.com", "Precious Oriafoh"),
    ("umeuche@gmail.com", "Lurd Uchay"),
    ("sarahejenobo@gmail.com", "Sarah Ejenobo"),
    ("bernnie4real@gmail.com", "Nweke Bernard"),
    ("nkemdirim.adeniji@gmail.com", "Kolade"),
    ("chubbythecreator@gmail.com", "Chubby"),
    ("saheedtundeakande@gmail.com", "Akande Saheed"),
    ("nnamaninora@yahoo.com", "Kachy"),
    ("uzomaokoli3@gmail.com", "Uzo"),
    ("namdy26@gmail.com", "Namdy"),
    ("abbeylala@gmail.com", "Abbey lala"),
    ("shay0002@yahoo.com", "Ogundimu Oluwasayo"),
    ("ronniematic015@gmail.com", "Ronnie"),
    ("insleeky4@gmail.com", "MissVanilla"),
    ("rachelmoses63@yahoo.com", "Rachel"),
    ("fynext83@gmail.com", "Fynext"),
    ("pegasusfem101@yahoo.com", "Stuffings"),
    ("igwilowinifred@yahoo.co.uk", "Igwilo winifred"),
    ("iffychuck@gmail.com", "Big4life"),
    ("afonjaoyindamola@gmail.com", "kels"),
    ("suleimonyusuf@gmail.com", "Yusuf Suleimon"),
    ("aishakane7@gmail.com", "Aisha kane"),
    ("chikaewah@gmail.com", "Chika Ewah"),
    ("bukonkolo@gmail.com", "Bukola"),
    ("superluvkid@gmail.com", "freshPrince"),
    ("agbaledesmond@gmail.com", "Dessta"),
    ("eziamakamc1@gmail.com", "Osari"),
    ("onaedopearl1801@gmail.com", "Babalawo"),
    ("charlesnwosu.cwc@gmail.com", "Charles Nwosu"),
    ("babatopealiu@gmail.com", "Babatope Aliu (BOA)"),
    ("tekraymond@gmail.com", "Tek Raymond"),
    ("harry_svc@yahoo.com", "Quickie"),
    ("henrychukwudum1@gmail.com", "Chukwudum Imagery"),
    ("emuwa.ekeh@gmail.com", "Emuwaegbulem Ekeh"),
    ("supamekynova9@gmail.com", "Miekam Womene"),
    ("desmondezebuiro@gmail.com", "Desmond"),
    ("tannyjimi5252@gmail.com", "BurgerMan"),
    ("writehandbrand@gmail.com", "Dede Dinma"),
    ("olukunle.falade@gmail.com", "Kunle"),
    ("chiemekejerry5@gmail.com", "Jerry Chiemeke"),
    ("ifeoluwaayano93@gmail.com", "Ifeoluwa Ayano"),
    ("kene90@hotmail.co.uk", "Uyaka"),
    ("gracechionye0@gmail.com", "McGuire"),
    ("lordchuma101@gmail.com", "Chucky"),
    ("kogboro@yahoo.co.uk", "Ken Ogboro"),
    ("tagbotee@gmail.com", "Tee Dot"),
    ("nneomanwamaka@me.com", "Nneoma Nocrap"),
    ("Dammylawal5@gmail.com", "Dammy lawall"),
    ("ibrahim.o.omotosho@gmail.com", "Heem"),
    ("apochieugene@gmail.com", "Sir Eugene Apochi"),
    ("urbanfleet@gmail.com", "Urban"),
    ("flexokosi@gmail.com", "Ozo white & white"),
    ("jessicaiyabo@gmail.com", "Lalatino"),
    ("adeltops@gmail.com", "Topsie"),
]


class Command(BaseCommand):
    help = "Generate random votes"

    def handle(self, *args, **options):

        for p in points:
            Point.objects.get_or_create(points=p)

        for p in people:
            email = p[0]
            name = p[1]

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

            self.stdout.write(self.style.SUCCESS(person))
