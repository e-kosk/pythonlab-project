from django.contrib.auth.models import User
from django.db import models


class Exercise(models.Model):
    title = models.CharField(max_length=64, verbose_name='tytuł')
    description = models.TextField(verbose_name='treść')
    award_points = models.PositiveSmallIntegerField(verbose_name='punkty za zadanie')
    code = models.OneToOneField('ExerciseCode', on_delete=models.CASCADE, null=True, verbose_name='kod')

    def __str__(self):
        return f'"{self.title}" {self.description[:40]}'


class ExerciseCode(models.Model):
    source_code = models.TextField(verbose_name='kod źródłowy')

    def __str__(self):
        return self.source_code[:40]


class Points(models.Model):
    points = models.PositiveSmallIntegerField(verbose_name='punkty', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='użytkownik')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, verbose_name='zadanie')

    class Meta:
        unique_together = ['user', 'exercise']


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent', verbose_name='od')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received', verbose_name='do')
    title = models.CharField(max_length=64, verbose_name='tytuł', null=True)
    text = models.TextField(verbose_name='treść')
    date = models.DateTimeField(auto_now=True, verbose_name='data')

    def get_short_text(self):
        return self.text[:40]

    def get_title(self):
        return self.title if self.title else '<brak tytułu>'

