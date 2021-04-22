from typing import Any, Dict
from django import forms
from django.forms.utils import pretty_name

from people.models import Person


class VoteForm(forms.Form):
    first_place = forms.ModelChoiceField(
        required=True,
        empty_label='Select first place',
        queryset=Person.objects.filter(is_contestant=True),
        widget=forms.Select(attrs={'class': 'form-control'}))

    second_place = forms.ModelChoiceField(
        required=True,
        empty_label='Select second place',
        queryset=Person.objects.filter(is_contestant=True),
        widget=forms.Select(attrs={'class': 'form-control'}))

    third_place = forms.ModelChoiceField(
        required=True,
        empty_label='Select third place',
        queryset=Person.objects.filter(is_contestant=True),
        widget=forms.Select(attrs={'class': 'form-control'}))

    def clean(self) -> Dict[str, Any]:
        first_place = self.cleaned_data['first_place']
        second_place = self.cleaned_data['second_place']
        third_place = self.cleaned_data['third_place']

        if first_place == second_place:
            self.add_error('second_place', 'Already selected')
            return

        if first_place == third_place:
            self.add_error('third_place', 'Already selected')
            return

        if second_place == third_place:
            self.add_error('third_place', 'Already selected')
            return


