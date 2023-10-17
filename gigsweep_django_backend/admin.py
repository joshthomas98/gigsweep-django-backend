from django.contrib import admin
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, ArtistGigApplication, VenueGigApplication

admin.site.register(Artist)
admin.site.register(Unavailability)
admin.site.register(Venue)
admin.site.register(ArtistListedGig)
admin.site.register(VenueListedGig)
admin.site.register(NewsletterSignup)
admin.site.register(MembershipOptions)
admin.site.register(ArtistWrittenReview)
admin.site.register(VenueWrittenReview)
admin.site.register(ArtistGigApplication)
admin.site.register(VenueGigApplication)
