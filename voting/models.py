from django.db import models

from utils.models import TimeStampedModel

class Point(TimeStampedModel):
    points = models.IntegerField(default=5)

    class Meta:
        ordering = ['points']

    def __str__(self) -> str:
        return f"{self.points} points"
