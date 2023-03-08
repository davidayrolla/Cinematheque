from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    re_path(r'^$', index, name='core_index'),
    re_path(r'index', index, name='core_index'),
    re_path(r'home', home, name='core_home'),

    re_path(r'userprofilelist', userprofileList, name='core_userprofile_list'),
    re_path(r'userprofileinsert', userprofileInsert, name='core_userprofile_insert'),
    re_path(r'userprofileupdate/(?P<id>\d+)/$', userprofileUpdate, name='core_userprofile_update'),
    re_path(r'userchangepicture/(?P<id>\d+)/$', userChangePicture, name='core_user_changepicture'),

    re_path(r'genrelist', genreList, name='core_genre_list'),
    re_path(r'genreinsert', genreInsert, name='core_genre_insert'),
    re_path(r'genreupdate/(?P<id>\d+)/$', genreUpdate, name='core_genre_update'),
    re_path(r'genredelete/(?P<id>\d+)/$', genreDelete, name='core_genre_delete'),

    re_path(r'countrylist', countryList, name='core_country_list'),
    re_path(r'countryinsert', countryInsert, name='core_country_insert'),
    re_path(r'countryupdate/(?P<id>\d+)/$', countryUpdate, name='core_country_update'),
    re_path(r'countrydelete/(?P<id>\d+)/$', countryDelete, name='core_country_delete'),

    re_path(r'rolelist', roleList, name='core_role_list'),
    re_path(r'roleinsert', roleInsert, name='core_role_insert'),
    re_path(r'roleupdate/(?P<id>\d+)/$', roleUpdate, name='core_role_update'),
    re_path(r'roledelete/(?P<id>\d+)/$', roleDelete, name='core_role_delete'),

    re_path(r'distributorlist', distributorList, name='core_distributor_list'),
    re_path(r'distributorinsert', distributorInsert, name='core_distributor_insert'),
    re_path(r'distributorupdate/(?P<id>\d+)/$', distributorUpdate, name='core_distributor_update'),
    re_path(r'distributordelete/(?P<id>\d+)/$', distributorDelete, name='core_distributor_delete'),

    re_path(r'languagelist', languageList, name='core_language_list'),
    re_path(r'languageinsert', languageInsert, name='core_language_insert'),
    re_path(r'languageupdate/(?P<id>\d+)/$', languageUpdate, name='core_language_update'),
    re_path(r'languagedelete/(?P<id>\d+)/$', languageDelete, name='core_language_delete'),

    re_path(r'typeofartworklist', typeofartworkList, name='core_typeofartwork_list'),
    re_path(r'typeofartworkinsert', typeofartworkInsert, name='core_typeofartwork_insert'),
    re_path(r'typeofartworkupdate/(?P<id>\d+)/$', typeofartworkUpdate, name='core_typeofartwork_update'),
    re_path(r'typeofartworkdelete/(?P<id>\d+)/$', typeofartworkDelete, name='core_typeofartwork_delete'),

    re_path(r'personlist', personList, name='core_person_list'),
    re_path(r'personinsert', personInsert, name='core_person_insert'),
    re_path(r'personupdate/(?P<id>\d+)/$', personUpdate, name='core_person_update'),
    re_path(r'persondelete/(?P<id>\d+)/$', personDelete, name='core_person_delete'),

    re_path(r'artworklist', artworkList, name='core_artwork_list'),
    re_path(r'artworkinsert', artworkInsert, name='core_artwork_insert'),
    re_path(r'artworkupdate/(?P<id>\d+)/$', artworkUpdate, name='core_artwork_update'),
    re_path(r'artworkdelete/(?P<id>\d+)/$', artworkDelete, name='core_artwork_delete'),

]