from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Value, IntegerField
from people.models import Person


@login_required
def leaderboard(request):
    context = {}

    context["persons"] = (
        Person.objects.filter(is_contestant=True)
        .annotate(
            total_points=Sum("contestant__point__points"),
        )
        .order_by("-total_points")
    )

    template = "voting/leaderboard.html"
    return render(request, template, context)
