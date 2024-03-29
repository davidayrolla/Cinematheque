from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Coalesce
import django.db.utils
from django.core.paginator import Paginator
from .forms import *


#Quantidade de itens por página nas consultas
list_page_count = 10


def index(request):
    artwork = Artwork.objects.latest('DateTimeOfLastUpdate')
    person = Person.objects.latest('DateTimeOfLastUpdate')

    data = {
        'latestartwork': artwork,
        'latestperson': person,
    }

    return render(request, 'core/index.html', data )


def home(request):

    if request.user.is_authenticated:
        artwork = Artwork.objects.latest('DateTimeOfLastUpdate')
        person = Person.objects.latest('DateTimeOfLastUpdate')
        numartworks = Artwork.objects.all().count()
        numpeople = Person.objects.all().count()

        data = {
            'latestartwork': artwork,
            'latestperson': person,
            'numartworks': numartworks,
            'numpeople': numpeople,
            'userProfile': UserProfile.objects.get(User=request.user),
        }

        return render(request, 'core/home.html', data )

    else:
        return redirect('login')


def search(request):
    strtoSearch = request.GET['texttoSearch'].strip()

    artworks = Artwork.objects.filter(
        Q( OriginalTitle__icontains = strtoSearch ) |
        Q( TitleEN__contains = strtoSearch ) |
        Q( TitlePT_BR__contains = strtoSearch) |
        Q( ReleaseYear__contains = strtoSearch) |
        Q( Country__NameEN__iexact = strtoSearch) |
        Q( Country__NamePT_BR__iexact = strtoSearch) |
        Q( Genres__NameEN__iexact = strtoSearch) |
        Q( Genres__NamePT_BR__iexact = strtoSearch)
    ).distinct().order_by('OriginalTitle')

    pagArtwork = Paginator(artworks, list_page_count )
    page_number = request.GET.get("pagart")
    pageart_obj = pagArtwork.get_page(page_number)

    persons = Person.objects.filter(
        Q( Name__icontains = strtoSearch ) |
        Q( DateOfBirth__contains = strtoSearch) |
        Q( DateOfDeath__contains = strtoSearch) |
        Q( CountryOfBirth__NameEN__iexact = strtoSearch) |
        Q( CountryOfBirth__NamePT_BR__iexact = strtoSearch)
    ).order_by('Name')

    pagPerson = Paginator(persons, list_page_count )
    page_number = request.GET.get("pagper")
    pageper_obj = pagPerson.get_page(page_number)

    data = {'strtosearch': strtoSearch,
            'pageart_obj': pageart_obj,
            'pageper_obj': pageper_obj,
            }

    return render(request, 'core/resultssearch.html', data )


#-------- Userprofile views
@login_required
def userprofileList(request):
    usersprofiles = UserProfile.objects.all().order_by('User')

    paginator = Paginator(usersprofiles, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': UserProfile,
            'page_obj': page_obj}
    return render(request, 'core/userprofilelist.html', data )


@login_required
def userprofileInsert(request):
    if request.method == 'GET':
        data = {}
        userprofile = UserProfile()
        form = UserProfileForm(instance=userprofile)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
        data['object'] = userprofile
        data['form'] = form
        return render(request, 'core/userprofileinsert.html', data)
    else:
        form = UserProfileForm( request.POST or None, request.FILES or None )
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.InsertUser = request.user
            userprofile.save()
        return redirect('core_userprofile_list')


@login_required
def userprofileUpdate(request, id):
    data = {}
    userprofile = UserProfile.objects.get(id=id)
    form = UserProfileForm( request.POST or None, request.FILES or None, instance=userprofile)
    data['userProfile'] = UserProfile.objects.get(User=request.user)
    data['object'] = userprofile
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.LastUpdateUser = request.user
            userprofile.save()
            return redirect('core_userprofile_list')
    else:
        return render(request, 'core/userprofileupdate.html', data)


@login_required
def userChangePicture(request, id):
    data = {}
    userprofile = UserProfile.objects.get(id=id)
    form = UserChangePictureForm( request.POST or None, request.FILES or None, instance=userprofile)
    data['userProfile'] = UserProfile.objects.get(User=request.user)
    data['object'] = userprofile
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.LastUpdateUser = request.user
            userprofile.save()
            return redirect('core_home')
    else:
        return render(request, 'core/userchangepicture.html', data)


@login_required
def userprofileDelete(request, id):
    userprofile = UserProfile.objects.get(id=id)
    if request.method == 'POST':
        try:
            userprofile.delete()
            return redirect('core_userprofile_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': userprofile,
               }
        return render(request, 'core/delete_confirm.html', data )


#-------- Genre views

@login_required
def genreList(request):
    genres = Genre.objects.all().order_by('NameEN')

    paginator = Paginator(genres, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Genre,
            'page_obj': page_obj }
    return render(request, 'core/genrelist.html', data )


@login_required
def genreInsert(request):
    if request.method == 'GET':
        data = {}
        genre = Genre()
        form = GenreForm(instance=genre)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
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
    data['userProfile'] = UserProfile.objects.get(User=request.user)
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
        try:
            genre.delete()
            return redirect('core_genre_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': genre,
               }
        return render(request, 'core/delete_confirm.html', data )



#-------- Country views

@login_required
def countryList(request):
    countries = Country.objects.all().order_by('NameEN')

    paginator = Paginator(countries, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Country,
            'page_obj': page_obj }
    return render(request, 'core/countrylist.html', data )


@login_required
def countryInsert(request):
    if request.method == 'GET':
        data = {}
        country = Country()
        form = CountryForm(instance=country)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
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
    data['userProfile'] = UserProfile.objects.get(User=request.user)
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
        try:
            country.delete()
            return redirect('core_country_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': country,
               }
        return render(request, 'core/delete_confirm.html', data )




#-------- Role views

@login_required
def roleList(request):
    roles = Role.objects.all().order_by('NameEN')

    paginator = Paginator(roles, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Role,
            'page_obj': page_obj }

    return render(request, 'core/rolelist.html', data )


@login_required
def roleInsert(request):
    if request.method == 'GET':
        data = {}
        role = Role()
        form = RoleForm(instance=role)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
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
    data['userProfile'] = UserProfile.objects.get(User=request.user)
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
        try:
            role.delete()
            return redirect('core_role_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': role,
               }
        return render(request, 'core/delete_confirm.html', data )



#-------- Distributor views

@login_required
def distributorList(request):
    distributors = Distributor.objects.all().order_by('Name')

    paginator = Paginator(distributors, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Distributor,
            'page_obj': page_obj}

    return render(request, 'core/distributorlist.html', data )


@login_required
def distributorInsert(request):
    if request.method == 'GET':
        data = {}
        distributor = Distributor()
        form = DistributorForm(instance=distributor)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
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
    data['userProfile'] = UserProfile.objects.get(User=request.user)
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
        try:
            distributor.delete()
            return redirect('core_distributor_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': distributor,
               }
        return render(request, 'core/delete_confirm.html', data )



#-------- Language views

@login_required
def languageList(request):
    languages = Language.objects.all().order_by('NameEN')

    paginator = Paginator(languages, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Language,
            'page_obj': page_obj }

    return render(request, 'core/languagelist.html', data )


@login_required
def languageInsert(request):
    if request.method == 'GET':
        data = {}
        language = Language()
        form = LanguageForm(instance=language)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
        data['object'] = language
        data['form'] = form
        return render(request, 'core/languageinsert.html', data)
    else:
        form = LanguageForm( request.POST or None, request.FILES or None )
        if form.is_valid():
            language = form.save(commit=False)
            language.InsertUser = request.user
            language.save()
        return redirect('core_language_list')


@login_required
def languageUpdate(request, id):
    data = {}
    language = Language.objects.get(id=id)
    form = LanguageForm( request.POST or None, request.FILES or None, instance=language)
    data['userProfile'] = UserProfile.objects.get(User=request.user)
    data['object'] = language
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            language = form.save(commit=False)
            language.LastUpdateUser = request.user
            language.save()
            return redirect('core_language_list')
    else:
        return render(request, 'core/languageupdate.html', data)


@login_required
def languageDelete(request, id):
    language = Language.objects.get(id=id)
    if request.method == 'POST':
        try:
            language.delete()
            return redirect('core_language_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': language,
               }
        return render(request, 'core/delete_confirm.html', data )



#-------- TypeOfArtwork views

@login_required
def typeofartworkList(request):
    typesofartwork = TypeOfArtwork.objects.all().order_by('NameEN')

    paginator = Paginator(typesofartwork, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': TypeOfArtwork,
            'page_obj': page_obj }

    return render(request, 'core/typeofartworklist.html', data )


@login_required
def typeofartworkInsert(request):
    if request.method == 'GET':
        data = {}
        typeofartwork = TypeOfArtwork()
        form = TypeOfArtworkForm(instance=typeofartwork)
        data['userProfile'] = UserProfile.objects.get(User=request.user)
        data['object'] = typeofartwork
        data['form'] = form
        return render(request, 'core/typeofartworkinsert.html', data)
    else:
        form = TypeOfArtworkForm( request.POST or None, request.FILES or None )
        if form.is_valid():
            typeofartwork = form.save(commit=False)
            typeofartwork.InsertUser = request.user
            typeofartwork.save()
        return redirect('core_typeofartwork_list')


@login_required
def typeofartworkUpdate(request, id):
    data = {}
    typeofartwork = TypeOfArtwork.objects.get(id=id)
    form = TypeOfArtworkForm( request.POST or None, request.FILES or None, instance=typeofartwork)
    data['userProfile'] = UserProfile.objects.get(User=request.user)
    data['object'] = typeofartwork
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            typeofartwork = form.save(commit=False)
            typeofartwork.LastUpdateUser = request.user
            typeofartwork.save()
            return redirect('core_typeofartwork_list')
    else:
        return render(request, 'core/typeofartworkupdate.html', data)


@login_required
def typeofartworkDelete(request, id):
    typeofartwork = TypeOfArtwork.objects.get(id=id)
    if request.method == 'POST':
        try:
            typeofartwork.delete()
            return redirect('core_typeofartwork_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': typeofartwork,
               }
        return render(request, 'core/delete_confirm.html', data )



#-------- Person views

@login_required
def personList(request):
    persons = Person.objects.all().order_by('Name')

    paginator = Paginator(persons, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Person,
            'page_obj': page_obj }

    return render(request, 'core/personlist.html', data )


@login_required
def personInsert(request):
    person = Person()
    item_membership_formset = inlineformset_factory(Person, Membership, form=MembershipForm, extra=3, can_delete=False,
                                                    min_num=0, validate_min=False)
    if request.method == 'GET':
        data = {}
        form = PersonForm(instance=person, prefix='main')
        formset = item_membership_formset(instance=person, prefix='membership')
        data['userProfile'] = UserProfile.objects.get(User=request.user)
        data['object'] = person
        data['form'] = form
        data['formset'] = formset
        return render(request, 'core/personinsert.html', data)
    else:
        form = PersonForm( request.POST or None, request.FILES or None, instance=person, prefix='main' )
        formset = item_membership_formset(request.POST, request.FILES, instance=person, prefix='membership')
        if form.is_valid():
            try:
                person = form.save(commit=False)
                person.InsertUser = request.user
                person.save()
                formset.save()
            except ValueError:
                pass
        return redirect('core_person_list')


@login_required
def personUpdate(request, id):
    data = {}
    person = Person.objects.get(id=id)
    item_membership_formset = inlineformset_factory(Person, Membership, form=MembershipForm, extra=3, can_delete=True,
                                                    min_num=0, validate_min=False)
    form = PersonForm( request.POST or None, request.FILES or None, instance=person, prefix='main')
    formset = item_membership_formset(request.POST or None, instance=person, prefix='membership')
    formset.is_valid()
    data['userProfile'] = UserProfile.objects.get(User=request.user)
    data['object'] = person
    data['form'] = form
    data['formset'] = formset
    if request.method == 'POST':
        if form.is_valid():
            try:
                person = form.save(commit=False)
                person.LastUpdateUser = request.user
                person.save()
                formset.save()
            except ValueError:
                pass
            return redirect('core_person_list')
    else:
        return render(request, 'core/personupdate.html', data)


@login_required
def personDelete(request, id):
    person = Person.objects.get(id=id)
    if request.method == 'POST':
        try:
            person.delete()
            return redirect('core_person_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': person,
               }
        return render(request, 'core/delete_confirm.html', data )


def personData(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404

    artworks = Membership.objects.filter(Person=person).order_by('Role_id', 'Artwork__OriginalTitle')

    data = { 'person': person,
             'artworks': artworks}

    return render(request, 'core/persondata.html', data)




#-------- Artwork views

@login_required
def artworkList(request):
    artworks = Artwork.objects.all().order_by(Coalesce('TitleEN', 'OriginalTitle'))

    paginator = Paginator(artworks, list_page_count )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {'userProfile': UserProfile.objects.get(User=request.user),
            'class': Artwork,
            'page_obj': page_obj }
    return render(request, 'core/artworklist.html', data )


@login_required
def artworkInsert(request):
    artwork = Artwork()
    item_membership_formset = inlineformset_factory(Artwork, Membership, form=MembershipForm, extra=3, can_delete=False,
                                                    min_num=0, validate_min=False)
    if request.method == 'GET':
        data = {}
        form = ArtworkForm(instance=artwork, prefix='main')
        formset = item_membership_formset(instance=artwork, prefix='membership')
        data['userProfile'] = UserProfile.objects.get(User=request.user)
        data['object'] = artwork
        data['form'] = form
        data['formset'] = formset
        return render(request, 'core/artworkinsert.html', data)
    else:
        form = ArtworkForm( request.POST or None, request.FILES or None, instance=artwork, prefix='main' )
        formset = item_membership_formset(request.POST, request.FILES, instance=artwork, prefix='membership')
        if form.is_valid():
            try:
                artwork = form.save(commit=False)
                artwork.InsertUser = request.user
                artwork.save()
                form.save_m2m()
                formset.save()
            except ValueError:
                pass
        return redirect('core_artwork_list')


@login_required
def artworkUpdate(request, id):
    data = {}
    artwork = Artwork.objects.get(id=id)
    item_membership_formset = inlineformset_factory(Artwork, Membership, form=MembershipForm, extra=3, can_delete=True,
                                                    min_num=0, validate_min=False)
    form = ArtworkForm( request.POST or None, request.FILES or None, instance=artwork, prefix='main')
    formset = item_membership_formset(request.POST or None, instance=artwork, prefix='membership')
    formset.is_valid()
    data['userProfile'] = UserProfile.objects.get(User=request.user)
    data['object'] = artwork
    data['form'] = form
    data['formset'] = formset
    if request.method == 'POST':
        if form.is_valid(): # and formset.is_valid():
            try:
                artwork = form.save(commit=False)
                artwork.LastUpdateUser = request.user
                artwork.save()
                form.save_m2m()
                formset.save()
            except ValueError:
                pass
            return redirect('core_artwork_list')
    else:
        return render(request, 'core/artworkupdate.html', data)


@login_required
def artworkDelete(request, id):
    artwork = Artwork.objects.get(id=id)
    if request.method == 'POST':
        try:
            artwork.delete()
            return redirect('core_artwork_list')
        except Exception as err:
            if err.__class__ == django.db.utils.IntegrityError:
                data = {'userProfile': UserProfile.objects.get(User=request.user),
                        'errormessage': "Uh oh, this record cannot be delete because there is other data using it."}
                return render(request, 'core/errormessage.html', data)
    else:
        data = { 'userProfile': UserProfile.objects.get(User=request.user),
                 'obj': artwork,
               }
        return render(request, 'core/delete_confirm.html', data )


def artworkData(request, id):
    try:
        artwork = Artwork.objects.get(id=id)
    except Artwork.DoesNotExist:
        raise Http404

    members = Membership.objects.filter(Artwork=artwork).order_by('Role_id', 'Person__Name')

    data = { 'artwork': artwork,
             'members': members }

    return render(request, 'core/artworkdata.html', data)


