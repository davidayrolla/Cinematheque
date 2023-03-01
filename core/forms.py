from .models import *
from django.forms import ModelForm

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['NameEN', 'NamePT_BR']


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['NameEN', 'NamePT_BR', 'Flag']


class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['NameEN', 'NamePT_BR']


class DistributorForm(ModelForm):
    class Meta:
        model = Distributor
        fields = ['Name']


