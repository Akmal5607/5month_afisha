from django.urls import path
from tvshow.views import film_all_view, film_detail_view


urlpatterns = [
    path('film_list/', film_all_view, name='film_list'),
    path('film_list/<int:id>', film_detail_view, name='film_detail')
]