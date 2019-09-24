from learn_python.models import Exercise


def all_exercises(request):
    return {'exercises': Exercise.objects.all()}