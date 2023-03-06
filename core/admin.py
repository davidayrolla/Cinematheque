from django.contrib import admin
from .models import *


class MembershipInline(admin.TabularInline):
    model = Membership


class ArtworkAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Person, PersonAdmin)
admin.site.register(Distributor)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(TypeOfArtwork)
admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Membership)
admin.site.register(UserProfile)

