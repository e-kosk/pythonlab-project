from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

import os
import re

from learn_python.forms import *
from learn_python.models import Exercise, Points


class HomeView(View):

    def get(self, request):
        return render(request, 'learn_python/home.html')


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'base/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['login']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'base/login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('/login')


class ExerciseView(View):

    def get(self, request, exercise_id):
        exercise = Exercise.objects.get(pk=exercise_id)
        form = ExerciseForm()
        context = {
            'form': form,
            'exercise': exercise,
        }
        return render(request, 'learn_python/exercise.html', context)

    def post(self, request, exercise_id):
        number_of_tests_for_exercises = [1, 5]
        exercise = Exercise.objects.get(pk=exercise_id)
        form = ExerciseForm(request.POST)
        context = {
            'form': form,
            'exercise': exercise,
        }
        if form.is_valid():
            file = open('tmp_user.py', 'w')
            file.write(form.cleaned_data['code'])
            file.close()
            usr_size = os.stat('tmp_user.py').st_size

            file = open('tmp_exercise.py', 'w')
            file.write(str(exercise.code))
            file.close()
            ex_size = os.stat('tmp_exercise.py').st_size

            # Points.objects.create(
            #     user=request.user,
            #     exercise=exercise,
            #     points=exercise.award_points * (ex_size / usr_size)
            # )

            result = os.popen('pytest learn_python/test_exercises.py').read()

            pass_result = re.findall('learn_python\/test_exercises\.py (?P<pass_result>[F.]*)', result)[0]

            begin_tests_at = sum(number_of_tests_for_exercises[:exercise_id - 1])
            exercise_result = pass_result[begin_tests_at: begin_tests_at + number_of_tests_for_exercises[exercise_id-1]]

            print('DZIAŁA' if exercise_result == '.' else 'NIE DZIALA')
            # print('\n')
            # print(result)
            # print('\n')
            # print(exercise_result)

            context = {
                'exercise': exercise,
            }
            return render(request, 'learn_python/success.html', context)

        return render(request, 'learn_python/exercise.html', context)


class ExercisesView(View):
    pass
    # TODO


class AccountView(View):
    pass
    # TODO
