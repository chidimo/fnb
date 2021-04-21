from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F

from people.models import Person


@login_required
def person_profile(request, pk):
    context = {}

    context['person'] = Person.objects.get(pk=pk)

    template = 'people/profile.html'
    return render(request, template, context)


@login_required
def leaderboard(request):
    context = {}

    context["persons"] = (
        Person.objects.filter(is_contestant=True)
        .annotate(
            total_points=Sum("contestant__point__points"),
        )
        .order_by(F("total_points").desc(nulls_last=True), "name")
    )

    template = "people/leaderboard.html"
    return render(request, template, context)

@login_required
def all_persons(request):
    context = {}

    context["persons"] = (
        Person.objects.all()
    )

    template = "people/persons.html"
    return render(request, template, context)
