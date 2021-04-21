from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from voting.models import Point, Vote
from voting.forms import VoteForm


@login_required
def vote_screen(request):
    template = 'voting/vote.html'
    user = request.user
    person = user.person

    if request.method == 'POST':
        form = VoteForm(request.POST, user=user)
        if form.is_valid():
            data = form.cleaned_data
            print('form data', data)

            first = Point.objects.get(points=15)
            second = Point.objects.get(points=10)
            third = Point.objects.get(points=5)

            first_place = data['first_place']
            second_place = data['second_place']
            third_place = data['third_place']

            votes_cast = [
                { "point": first, "contestant": first_place, "voter": person},
                { "point": second, "contestant": second_place, "voter": person},
                { "point": third, "contestant": third_place, "voter": person},
            ]

            for v in votes_cast:
                Vote.objects.create(**v)

            return redirect('people:leaderboard')
        return render(request, template, {'form': form})

    return render(request, template, {'form': VoteForm()})
