from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from people.models import Person


@login_required
def personnel_detail(request, pk):
    context = {}

    context['person'] = Person.objects.get(pk=pk)

    template = 'people/profile.html'
    return render(request, template, context)
