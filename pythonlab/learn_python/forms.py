from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExerciseForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class AddExerciseForm(forms.Form):
    title = forms.CharField(max_length=64, label='tytuł')
    description = forms.CharField(widget=forms.Textarea, label='opis')
    award_points = forms.IntegerField(min_value=10, max_value=100, label='punkty')
    code = forms.CharField(widget=forms.Textarea, label='kod')
