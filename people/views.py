from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F

from people.models import Person
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


@login_required
def person_profile(request, pk):
    context = {}

    context["person"] = Person.objects.get(pk=pk)

    template = "people/profile.html"
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

    context["persons"] = Person.objects.all()

    template = "people/persons.html"
    return render(request, template, context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("people:profile", kwargs={"pk": user.pk})
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "people/change_password.html", {"form": form})
