from .models import *
from django.forms import ModelForm

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        fields = ['NameEN', 'NamePT_BR']


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        fields = ['NameEN', 'NamePT_BR']
