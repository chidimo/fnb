from typing import Any, Dict
from django import forms

from people.models import Person


class VoteForm(forms.Form):
    first_place = forms.ModelChoiceField(
        required=False,
        empty_label='Select first place',
        queryset=Person.objects.filter(is_contestant=True),
        widget=forms.Select(attrs={'class': 'form-control'}))

    second_place = forms.ModelChoiceField(
        required=False,
        empty_label='Select second place',
        queryset=Person.objects.filter(is_contestant=True),
        widget=forms.Select(attrs={'class': 'form-control'}))

    third_place = forms.ModelChoiceField(
        required=False,
        empty_label='Select third place',
        queryset=Person.objects.filter(is_contestant=True),
        widget=forms.Select(attrs={'class': 'form-control'}))

    def clean(self) -> Dict[str, Any]:
        first_place = self.cleaned_data['first_place']
        second_place = self.cleaned_data['second_place']
        third_place = self.cleaned_data['third_place']

        print('1', first_place)
        print('2', second_place)
        print('3', third_place)

        if first_place is None:
            self.add_error('first_place', 'Please select an option.')
            return

        if second_place is None:
            self.add_error('second_place', 'Please select an option.')
            return

        if third_place is None:
            self.add_error('third_place', 'Please select an option.')
            return


        if first_place == second_place:
            self.add_error('second_place', 'Already selected')
            return

        if first_place == third_place:
            self.add_error('third_place', 'Already selected')
            return

        if second_place == third_place:
            self.add_error('third_place', 'Already selected')
            return
