from django.db import models

from utils.models import TimeStampedModel
# from people.models import Person


class Point(TimeStampedModel):
    points = models.IntegerField(default=5)

    class Meta:
        ordering = ["points"]

    def __str__(self) -> str:
        return f"{self.points} points"


# class Vote(TimeStampedModel):
#     vote = models.ForeignKey(Point, on_delete=models.CASCADE)
#     voted_for = models.ForeignKey(
#         Person, on_delete=models.CASCADE, related_name="voted_for"
#     )
#     voter = models.ForeignKey(
#         Person, on_delete=models.SET_NULL, null=True, blank=True, related_name="voter"
#     )
