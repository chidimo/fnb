from django.db import models

from utils.models import TimeStampedModel
from people.models import Person


class Point(TimeStampedModel):
    points = models.IntegerField(default=5)

    class Meta:
        ordering = ["points"]

    def __str__(self) -> str:
        return f"{self.points} points"


class Vote(TimeStampedModel):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    contestant = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="contestant"
    )
    voter = models.ForeignKey(
        Person, on_delete=models.SET_NULL, null=True, blank=True, related_name="voter"
    )

    def __str__(self) -> str:
        return f"{self.voter.user.email} votes for {self.contestant.user.email}"
