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
            genre.InsertUserId = request.user
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
            genre.LastUpdateUserId = request.user
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

