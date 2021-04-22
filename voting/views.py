from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from voting.models import Point, Vote
from voting.forms import VoteForm


@login_required
def vote_screen(request):
    template = "voting/vote.html"
    user = request.user
    person = user.person

    voting_closed = settings.VOTING_CLOSED
    has_voted = Vote.objects.filter(voter__user=user).exists()

    context = {
        "form": VoteForm(),
        "has_voted": has_voted,
        "voting_closed": voting_closed,
    }

    if voting_closed:
        messages.info(request, "Voting is currently closed.")
        return render(request, template, context)

    if has_voted:
        messages.error(request, "You have already cast your votes.")
        return render(request, template, context)

    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            first = Point.objects.get(points=15)
            second = Point.objects.get(points=10)
            third = Point.objects.get(points=5)

            first_place = data["first_place"]
            second_place = data["second_place"]
            third_place = data["third_place"]

            votes_cast = [
                {"point": first, "contestant": first_place, "voter": person},
                {"point": second, "contestant": second_place, "voter": person},
                {"point": third, "contestant": third_place, "voter": person},
            ]

            for v in votes_cast:
                Vote.objects.create(**v)

            messages.success(request, "Vote registered successfully.")
            return redirect("accounts:leaderboard")
        return render(request, template, {"form": form})

    return render(request, template, context)
