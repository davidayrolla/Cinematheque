from django.urls import path, re_path, include
from .views import home

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'home', home, name='core_home'),
]