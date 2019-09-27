from django.urls import path, re_path

from learn_python.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('account/', AccountView.as_view(), name='account'),
    path('exercise/<int:exercise_id>/', ExerciseView.as_view(), name='exercise'),
    path('ranking/', RankingView.as_view(), name='ranking'),
    path('messages/', MessagesView.as_view(), name='messages'),
    path('messages/new/', NewMessageView.as_view(), name='new-messages'),
    path('messages/<int:message_id>/', MessageView.as_view(), name='message'),
    re_path(r'^[\w\/_-]+$', NotFoundView.as_view(), name='not-found')
]
