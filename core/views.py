from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django import template
register = template.Library()


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
            'class': Genre,
            'genres': genres}
    return render(request, 'core/genrelist.html', data )


@login_required
def genreInsert(request):
    if request.method == 'GET':
        data = {}
        genre = Genre()
        form = GenreForm(instance=genre)
        data['userName'] = request.user.username.capitalize()
        data['object'] = genre
        data['form'] = form
        return render(request, 'core/genreinsert.html', data)
    else:
        form = GenreForm( request.POST or None, request.FILES or None )
        if form.is_valid():
            genre = form.save(commit=False)
            genre.InsertUser = request.user
            genre.save()
        return redirect('core_genre_list')


@login_required
def genreUpdate(request, id):
    data = {}
    genre = Genre.objects.get(id=id)
    form = GenreForm( request.POST or None, request.FILES or None, instance=genre)
    data['userName'] = request.user.username.capitalize()
    data['object'] = genre
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
            'class': Country,
            'countries': countries}
    return render(request, 'core/countrylist.html', data )


@login_required
def countryInsert(request):
    if request.method == 'GET':
        data = {}
        country = Country()
        form = CountryForm(instance=country)
        data['userName'] = request.user.username.capitalize()
        data['object'] = country
        data['form'] = form
        return render(request, 'core/countryinsert.html', data)
    else:
        form = CountryForm( request.POST or None, request.FILES or None )
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
    data['object'] = country
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




#-------- Role views

@login_required
def roleList(request):
    roles = Role.objects.all()
    data = {'userName': request.user.username.capitalize(),
            'class': Role,
            'roles': roles}
    return render(request, 'core/rolelist.html', data )


@login_required
def roleInsert(request):
    if request.method == 'GET':
        data = {}
        role = Role()
        form = RoleForm(instance=role)
        data['userName'] = request.user.username.capitalize()
        data['object'] = role
        data['form'] = form
        return render(request, 'core/roleinsert.html', data)
    else:
        form = RoleForm( request.POST or None, request.FILES or None )
        if form.is_valid():
            role = form.save(commit=False)
            role.InsertUser = request.user
            role.save()
        return redirect('core_role_list')


@login_required
def roleUpdate(request, id):
    data = {}
    role = Role.objects.get(id=id)
    form = RoleForm( request.POST or None, request.FILES or None, instance=role)
    data['userName'] = request.user.username.capitalize()
    data['object'] = role
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            role = form.save(commit=False)
            role.LastUpdateUser = request.user
            role.save()
            return redirect('core_role_list')
    else:
        return render(request, 'core/roleupdate.html', data)


@login_required
def roleDelete(request, id):
    role = Role.objects.get(id=id)
    if request.method == 'POST':
        role.delete()
        return redirect('core_role_list')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': role})




#-------- Distributor views

@login_required
def distributorList(request):
    distributors = Distributor.objects.all()
    data = {'userName': request.user.username.capitalize(),
            'class': Distributor,
            'distributors': distributors}
    return render(request, 'core/distributorlist.html', data )


@login_required
def distributorInsert(request):
    if request.method == 'GET':
        data = {}
        distributor = Distributor()
        form = DistributorForm(instance=distributor)
        data['userName'] = request.user.username.capitalize()
        data['object'] = distributor
        data['form'] = form
        return render(request, 'core/distributorinsert.html', data)
    else:
        form = DistributorForm( request.POST or None, request.FILES or None )
        if form.is_valid():
            distributor = form.save(commit=False)
            distributor.InsertUser = request.user
            distributor.save()
        return redirect('core_distributor_list')


@login_required
def distributorUpdate(request, id):
    data = {}
    distributor = Distributor.objects.get(id=id)
    form = DistributorForm( request.POST or None, request.FILES or None, instance=distributor)
    data['userName'] = request.user.username.capitalize()
    data['object'] = distributor
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            distributor = form.save(commit=False)
            distributor.LastUpdateUser = request.user
            distributor.save()
            return redirect('core_distributor_list')
    else:
        return render(request, 'core/distributorupdate.html', data)


@login_required
def distributorDelete(request, id):
    distributor = Distributor.objects.get(id=id)
    if request.method == 'POST':
        distributor.delete()
        return redirect('core_distributor_list')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': distributor})




