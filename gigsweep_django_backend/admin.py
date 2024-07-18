from django.contrib import admin
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, ArtistGigApplication, VenueGigApplication, VenueNotification, ArtistNotification


class ArtistGigApplicationInline(admin.TabularInline):
    model = ArtistGigApplication
    extra = 0  # No extra empty forms


class ArtistListedGigAdmin(admin.ModelAdmin):
    inlines = [ArtistGigApplicationInline]


admin.site.register(Artist)
admin.site.register(Unavailability)
admin.site.register(Venue)
admin.site.register(ArtistListedGig, ArtistListedGigAdmin)
admin.site.register(VenueListedGig)
admin.site.register(NewsletterSignup)
admin.site.register(MembershipOptions)
admin.site.register(ArtistWrittenReview)
admin.site.register(VenueWrittenReview)
admin.site.register(ArtistGigApplication)
admin.site.register(VenueGigApplication)
admin.site.register(VenueNotification)
admin.site.register(ArtistNotification)
