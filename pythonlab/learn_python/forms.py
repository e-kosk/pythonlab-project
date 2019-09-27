from django import forms
from django.contrib.auth.models import User

from learn_python.models import Message


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExerciseForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='hasło')
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class NewMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('to_user', 'title', 'text')
