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
            points=Sum("voted_for__vote__points"),
        )
        .order_by("-points")
    )

    template = "voting/leaderboard.html"
    return render(request, template, context)
