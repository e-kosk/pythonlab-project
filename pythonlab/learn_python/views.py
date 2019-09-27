from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

import os
import re

from django.views.generic import CreateView

from learn_python.forms import *
from learn_python.models import Exercise, Points, ExerciseCode, Message


class HomeView(View):
    @method_decorator(login_required)
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


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'base/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            email = register_form.cleaned_data['email']
            User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'base/register.html', {'register_form': register_form})


class ExerciseView(View):
    @method_decorator(login_required)
    def get(self, request, exercise_id):
        try:
            exercise = get_object_or_404(Exercise, pk=exercise_id)
        except Http404:
            return redirect('/404/')
        form = ExerciseForm()
        context = {
            'form': form,
            'exercise': exercise,
        }
        return render(request, 'learn_python/exercise.html', context)

    def post(self, request, exercise_id):
        exercise = Exercise.objects.get(pk=exercise_id)
        form = ExerciseForm(request.POST)
        if form.is_valid():
            file = open('learn_python/temp/tmp_user.py', 'w')
            file.write(form.cleaned_data['code'])
            file.close()
            file = open('learn_python/temp/tmp_user.py', 'r')
            file.seek(0)
            usr_size = len(file.read())
            file.close()

            file = open('learn_python/temp/tmp_exercise.py', 'w')
            file.write(str(exercise.code.source_code))
            file.close()
            file = open('learn_python/temp/tmp_exercise.py', 'r')
            file.seek(0)
            ex_size = len(file.read())
            file.close()

            function_name = re.findall(r'^def (?P<function_name>[a-zA-Z0-9_]*)\(', str(exercise.code))[0]

            result = os.popen(f'pytest learn_python/exercises_tests/test_{function_name}.py').read()

            pass_result = \
                re.findall(f'learn_python\/exercises_tests\/test_{function_name}\.py (?P<pass_result>[F.]*)', result)[0]

            context = {
                'exercise': exercise,
            }

            if pass_result == '.':
                user_score = round(exercise.award_points * (ex_size / usr_size))
                if user_score > exercise.award_points:
                    user_score = exercise.award_points
                context['user_score'] = user_score
                context['max_score'] = exercise.award_points
                context['next_id'] = exercise_id + 1
                try:
                    Points.objects.create(
                        user=request.user,
                        exercise=exercise,
                        points=exercise.award_points * (ex_size / usr_size)
                    )
                except IntegrityError:
                    context['already_done'] = True
                    pts = Points.objects.get(user=request.user, exercise=exercise)
                    pts.points = user_score
                    pts.save()
                return render(request, 'learn_python/success.html', context)

        context = {
            'form': form,
            'exercise': exercise,
            'wrong_code': True,
        }
        return render(request, 'learn_python/exercise.html', context)


class AccountView(View):
    @method_decorator(login_required)
    def get(self, request):
        user_points = sum([points.points for points in Points.objects.filter(user=request.user)])
        context = {
            'user_points': user_points,
        }
        return render(request, 'learn_python/account.html', context)

    def post(self, request):
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('account')


class RankingView(View):
    @method_decorator(login_required)
    def get(self, request):
        users = User.objects.all()

        users_points_and_id = []
        for user in users:
            users_points_and_id.append((sum([points.points for points in Points.objects.filter(user=user)]), user.id))

        sorted_users = sorted(users_points_and_id, key=lambda tup: tup[0], reverse=True)

        users_tuple = []
        for res in sorted_users:
            users_tuple.append((User.objects.get(pk=res[1]), res[0]))

        context = {
            'users_tuple': users_tuple,
        }
        return render(request, 'learn_python/ranking.html', context)


class MessagesView(View):
    @method_decorator(login_required)
    def get(self, request):
        messages = Message.objects.filter(to_user=request.user)
        context = {
            'messages': messages,
        }
        return render(request, 'learn_python/messages.html', context)


class NewMessageView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = NewMessageForm()
        context = {
            'form': form,
        }
        return render(request, 'learn_python/new_message.html', context)

    def post(self, request):
        form = NewMessageForm(request.POST)
        form.from_user = request.user
        if form.is_valid():
            Message.objects.create(
                from_user=request.user,
                to_user=form.cleaned_data['to_user'],
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
            )
            return redirect('messages')
        context = {
            'form': form,
        }
        return render(request, 'learn_python/new_message.html', context)


class MessageView(View):
    @method_decorator(login_required)
    def get(self, request, message_id):
        try:
            message = get_object_or_404(Message, pk=message_id)
        except Http404:
            return redirect('/404/')
        context = {
            'message': message,
        }
        return render(request, 'learn_python/message.html', context)


class NotFoundView(View):

    def get(self, request):
        return render(request, 'base/not_found.html')
