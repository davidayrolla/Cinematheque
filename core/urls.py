from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='core_index'),
    re_path(r'index', index, name='core_index'),
    re_path(r'home', home, name='core_home'),

    re_path(r'genrelist', genreList, name='core_genre_list'),
    re_path(r'genreinsert', genreInsert, name='core_genre_insert'),
    re_path(r'genreupdate/(?P<id>\d+)/$', genreUpdate, name='core_genre_update'),
    re_path(r'genredelete/(?P<id>\d+)/$', genreDelete, name='core_genre_delete'),

    re_path(r'countrylist', countryList, name='core_country_list'),
    re_path(r'countryinsert', countryInsert, name='core_country_insert'),
    re_path(r'countryupdate/(?P<id>\d+)/$', countryUpdate, name='core_country_update'),
    re_path(r'countrydelete/(?P<id>\d+)/$', countryDelete, name='core_country_delete'),

]