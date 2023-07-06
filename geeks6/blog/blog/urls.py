
from django.contrib import admin
from django.urls import path

from posts.views import hello_view, redict_to_youtube_view, google, git

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('youtube/', redict_to_youtube_view),
    path('google/', google),
    path('youtube/', git),
]
