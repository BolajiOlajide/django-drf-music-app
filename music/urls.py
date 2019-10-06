from django.urls import path
from music.views import ListSongsView, LoginView, RegisterUsersView


urlpatterns = [
    path("songs/", ListSongsView.as_view(), name="songs-all"),
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register")
]
