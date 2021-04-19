'''forms'''

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


Person = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))


class PersonCreationForm(forms.ModelForm):
    '''Custom UCF. Takes the standard
    variables of 'email', 'password1', 'password2'
    For creating instances of 'Person'.'''
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Re-enter Password', widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ('email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        Pers = super(PersonCreationForm, self).save(commit=False)
        Pers.set_password(self.cleaned_data['password1'])
        if commit:
            Pers.save()
        return Pers


class PersonChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = Person
        fields = ('email', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']
