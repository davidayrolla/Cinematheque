from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    About = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.User.username

    def is_superuser(self):
        return self.User.is_superuser

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'


class Base(models.Model):
    DateTimeOfInsert = models.DateTimeField(auto_now_add=True,auto_now=False)
    DateTimeOfLastUpdate = models.DateTimeField(auto_now=True)
    InsertUser = models.ForeignKey( settings.AUTH_USER_MODEL, null=True, blank=True,
                                    on_delete=models.CASCADE, related_name='+' )
    LastUpdateUser = models.ForeignKey( settings.AUTH_USER_MODEL, null=True, blank=True,
                                         on_delete=models.CASCADE, related_name='+' )

    class Meta:
        abstract = True


class Country(Base):
    NameEN = models.CharField(max_length=60)
    NamePT_BR = models.CharField(max_length=60)
    Flag = models.ImageField(upload_to='countries_flags/', null=True, blank=True)

    def __str__(self):
        return self.NameEN

    class Meta:
        verbose_name_plural = 'countries'


class Role(Base):
    NameEN = models.CharField(max_length=30)
    NamePT_BR = models.CharField(max_length=30)

    def __str__(self):
        return self.NameEN


class Person(Base):
    Name = models.CharField(max_length=60)
    DateOfBirth = models.DateField(auto_now=False, null=True, blank=True)
    DateOfDeath = models.DateField(auto_now=False, null=True, blank=True)
    CountryOfBirth = models.ForeignKey(Country, null=True, blank=True, on_delete=models.DO_NOTHING)
    Photo = models.ImageField(upload_to='person_photos', null=True, blank=True)

    def __str__(self):
        return self.Name


class Genre(Base):
    NameEN = models.CharField(max_length=30)
    NamePT_BR = models.CharField(max_length=30)

    def __str__(self):
        return self.NameEN


class TypeOfArtwork(Base):
    NameEN = models.CharField(max_length=30)
    NamePT_BR = models.CharField(max_length=30)

    def __str__(self):
        return self.NameEN

    class Meta:
        verbose_name = 'Type of Artwork'
        verbose_name_plural = 'Types of Artwork'


class Distributor(Base):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Language(Base):
    NameEN = models.CharField(max_length=30)
    NamePT_BR = models.CharField(max_length=30)

    def __str__(self):
        return self.NameEN


class Artwork(Base):
    OriginalTitle = models.CharField(max_length=100)
    TitleEN = models.CharField(max_length=100, null=True, blank=True)
    TitlePT_BR = models.CharField(max_length=100, null=True, blank=True)
    ReleaseYear = models.IntegerField(null=True, blank=True)
    RunTime = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to='artwork_photos', null=True, blank=True)
    OriginalLanguage = models.ForeignKey(Language, null=True, blank=True, on_delete=models.DO_NOTHING)
    Country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.DO_NOTHING)
    Genres = models.ManyToManyField(Genre, null=True, blank=True)
    Distributors = models.ManyToManyField(Distributor, null=True, blank=True)
    Members = models.ManyToManyField(Person, null=True, blank=True, through='Membership')

    def __str__(self):
        return self.TitleEN if self.TitleEN else self.OriginalTitle

    def listGenres(self):
        all_genres = list( self.Genres.values('NameEN') )
        result = ""
        for genre in all_genres:
            result += genre['NameEN'] + ', '
        return result[:-2]


class Membership(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Artwork} - {self.Person} ({self.Role})'

