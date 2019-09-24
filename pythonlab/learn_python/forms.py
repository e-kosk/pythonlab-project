from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExerciseForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)