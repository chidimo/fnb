from django.db import models

from utils.models import TimeStampedModel

class Vote(TimeStampedModel):
    points = models.IntegerField(default=5)

    class Meta:
        ordering = ['points']

    def __str__(self) -> str:
        return f"Vote with {self.points} points"
