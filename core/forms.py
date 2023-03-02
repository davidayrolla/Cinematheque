from .models import *
from django.forms import ModelForm, forms, widgets
from django.core.files.images import get_image_dimensions

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def clean_picture(self):
        picture = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(picture)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = picture.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(picture) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return picture


class UserChangePictureForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #         super(UserChangePictureForm, self).__init__(*args, **kwargs)
    #         self.fields['User'].widget = widgets.HiddenInput
    #         # self.fields['User'].widget.attrs['readonly'] = True

    def clean_picture(self):
        picture = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(picture)

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = picture.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(picture) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return picture

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


class LanguageForm(ModelForm):
    class Meta:
        model = Language
        fields = ['NameEN', 'NamePT_BR']


class TypeOfArtworkForm(ModelForm):
    class Meta:
        model = TypeOfArtwork
        fields = ['NameEN', 'NamePT_BR']


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['Name', 'DateOfBirth', 'DateOfDeath', 'CountryOfBirth', 'Photo']


class ArtworkForm(ModelForm):
    class Meta:
        model = Artwork
        fields = ['OriginalTitle', 'TitleEN', 'TitlePT_BR', 'ReleaseYear', 'RunTime',
                  'OriginalLanguage', 'Country', 'Genres', 'Distributors', 'Members', 'Image']




