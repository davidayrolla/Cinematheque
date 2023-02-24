from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'home', home, name='core_home'),

    re_path(r'genrelist', genreList, name='core_genre_list'),
    re_path(r'genreinsert', genreInsert, name='core_genre_insert'),
    re_path(r'genreupdate/(?P<id>\d+)/$', genreUpdate, name='core_genre_update'),
    re_path(r'genredelete/(?P<id>\d+)/$', genreDelete, name='core_genre_delete'),
]