from django.db import models


class Base(models.Model):
    DateTimeOfInsert = models.DateTimeField(auto_now=True)
    DateTimeOfLastUpdate = models.DateTimeField(auto_now=False, null=True, blank=True)
    InsertUserId = models.IntegerField()
    LastUpdateUserId = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Country(Base):
    NameEN = models.CharField(max_length=60)
    NamePT_BR = models.CharField(max_length=60)
    Flag = models.ImageField(upload_to='countries_flags', null=True, blank=True)

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
    CountryOfBirth = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
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
        verbose_name_plural = 'types of artwork'


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
    OriginalName = models.CharField(max_length=100)
    NameEN = models.CharField(max_length=100, null=True, blank=True)
    NamePT_BR = models.CharField(max_length=100, null=True, blank=True)
    ReleaseYear = models.IntegerField(null=True, blank=True)
    RunTime = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to='artwork_photos', null=True, blank=True)
    OriginalLanguage = models.ForeignKey(Language, null=True, blank=True, on_delete=models.DO_NOTHING)
    Genres = models.ManyToManyField(Genre, blank=True, null=True)

    def __str__(self):
        return self.NameEN if self.NameEN else self.OriginalName
