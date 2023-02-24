from .models import *
from django.forms import ModelForm

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        fields = ['NameEN', 'NamePT_BR']
