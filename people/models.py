"""Models"""

from django.db.models import Sum
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _

from utils.models import TimeStampedModel


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("You must provide an email address")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="email address")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    join_date = models.DateTimeField(default=timezone.now)

    objects = AppUserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return f"AppUser: {self.email}"

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        try:
            return self.personnel == obj.personnel
        except AttributeError:
            if self.is_admin:
                return True

    @property
    def is_staff(self):
        return self.is_admin


class Person(TimeStampedModel):
    class SexChoices(models.TextChoices):
        NA = "NA", _("Not applicable")
        MALE = "MALE", _("Male")
        FEMALE = "FEMALE", _("Female")

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    sex = models.CharField(
        max_length=10, choices=SexChoices.choices, default=SexChoices.NA
    )

    is_contestant = models.BooleanField(default=False)

    name = models.CharField(max_length=50)
    profile_pix = models.URLField(max_length=500, blank=True)
    phone = models.CharField(max_length=15, default="", blank=True)

    class Meta:
        verbose_name_plural = "persons"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name

    @property
    def has_voted(self):
        return len(self.votes_cast) > 0

    @property
    def str__admin(self):
        return f"Person: {self.name} ({self.user.email})"

    def save(self, *args, **kwargs):
        if not self.profile_pix:
            self.profile_pix = "https://via.placeholder.com/150/424897?text=avatar"
        super(Person, self).save(*args, **kwargs)

    def username(self):
        return self.user.email

    @property
    def received_votes(self):
        return self.contestant.aggregate(total=Sum("point__points"))["total"]

    @property
    def votes_cast(self):
        return [each.contestant.user.email for each in self.voter.all()]
