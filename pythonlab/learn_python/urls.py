from django.urls import path

from learn_python.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('exercises/', ExercisesView.as_view(), name='exercises'),
    path('exercise/<int:exercise_id>/', ExerciseView.as_view(), name='exercise'),
]