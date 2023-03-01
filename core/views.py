from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *



def index(request):
    return render(request, 'core/index.html' )


def home(request):
    data = {'userName': request.user.username.capitalize()}
    return render(request, 'core/home.html', data )


#-------- Genre views

@login_required
def genreList(request):
    genres = Genre.objects.all()
    data = {'userName': request.user.username.capitalize(),
            'className' : Genre.__name__,
            'genres': genres}
    return render(request, 'core/genrelist.html', data )


@login_required
def genreInsert(request):
    if request.method == 'GET':
        data = {}
        genre = Genre()
        form = GenreForm(instance=genre)
        data['userName'] = request.user.username.capitalize()
        data['className'] = Genre.__name__
        data['genre'] = genre
        data['form'] = form
        return render(request, 'core/genreinsert.html', data)
    else:
        form = GenreForm( request.POST or None )
        if form.is_valid():
            genre = form.save(commit=False)
            genre.InsertUser = request.user
            genre.save()
        return redirect('core_genre_list')


@login_required
def genreUpdate(request, id):
    data = {}
    genre = Genre.objects.get(id=id)
    form = GenreForm( request.POST or None, instance=genre)
    data['userName'] = request.user.username.capitalize()
    data['className'] = Genre.__name__
    data['object'] = genre
    data['genre'] = genre
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            genre = form.save(commit=False)
            genre.LastUpdateUser = request.user
            genre.save()
            return redirect('core_genre_list')
    else:
        return render(request, 'core/genreupdate.html', data)


@login_required
def genreDelete(request, id):
    genre = Genre.objects.get(id=id)
    if request.method == 'POST':
        genre.delete()
        return redirect('core_genre_list')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': genre})


#-------- Country views

@login_required
def countryList(request):
    countries = Country.objects.all()
    data = {'userName': request.user.username.capitalize(),
            'className' : Country.__name__,
            'countries': countries}
    return render(request, 'core/countrylist.html', data )


@login_required
def countryInsert(request):
    if request.method == 'GET':
        data = {}
        country = Country()
        form = CountryForm(instance=country)
        data['userName'] = request.user.username.capitalize()
        data['className'] = Country.__name__
        data['country'] = country
        data['form'] = form
        return render(request, 'core/countryinsert.html', data)
    else:
        form = CountryForm( request.POST, request.FILES )
        if form.is_valid():
            country = form.save(commit=False)
            country.InsertUser = request.user
            country.save()
        return redirect('core_country_list')


@login_required
def countryUpdate(request, id):
    data = {}
    country = Country.objects.get(id=id)
    form = CountryForm( request.POST or None, request.FILES or None, instance=country)
    data['userName'] = request.user.username.capitalize()
    data['className'] = Country.__name__
    data['object'] = country
    data['country'] = country
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            country = form.save(commit=False)
            country.LastUpdateUser = request.user
            country.save()
            return redirect('core_country_list')
    else:
        return render(request, 'core/countryupdate.html', data)


@login_required
def countryDelete(request, id):
    country = Country.objects.get(id=id)
    if request.method == 'POST':
        country.delete()
        return redirect('core_country_list')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': country})


