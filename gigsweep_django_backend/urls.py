from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('artists/', views.artist_list),
    path('artists/<int:id>/', views.artist_detail),

    path('unavailabilities/', views.unavailability_list),
    path('unavailabilities/<int:id>/', views.unavailability_detail),

    path('venues/', views.venue_list),
    path('venues/<int:id>/', views.venue_detail),

    path('artists/validate/', views.artist_sign_in),
    path('venues/validate/', views.venue_sign_in),

    path('artist_listed_gigs/', views.artist_listed_gig_list),
    path('artist_listed_gigs/<int:id>/', views.artist_listed_gig_detail),

    path('venue_listed_gigs/', views.venue_listed_gig_list),
    path('venue_listed_gigs/<int:id>/', views.venue_listed_gig_detail),

    path('artists/<int:artist_id>/listed_gigs/',
         views.artist_listed_gigs_by_artist),
    path('venues/<int:venue_id>/listed_gigs/',
         views.venue_listed_gigs_by_venue),

    path('artist_search/', views.artist_search),

    path('newslettersignups/', views.newsletter_signup_list),
    path('newslettersignups/<int:id>/', views.newsletter_signup_detail),

    path('featuredartists/', views.featured_artist_list),

    path('membershipoptions/', views.membership_option_list),
    path('membershipoptions/<int:id>/', views.membership_option_detail),

    # path('artist_listed_gig_search/', views.artist_listed_gig_search),

    # path('venue_listed_gig_search/', views.venue_listed_gig_search),

    path('gig_search/', views.gig_search),

    path('artist_written_reviews/', views.artist_written_review_list),
    path('artist_written_reviews/<int:id>/',
         views.artist_written_review_detail),

    path('venue_written_reviews/', views.venue_written_review_list),
    path('venue_written_reviews/<int:id>/', views.venue_written_review_detail),

    path('artist_written_review_check_profanities/',
         views.artist_written_review_check_profanities),

    path('venue_written_review_check_profanities/',
         views.venue_written_review_check_profanities),

    path('artists/search/', views.search_bar_artists),
    path('venues/search/', views.search_bar_venues),

    path('artistgigapplications/', views.artist_gig_application_list),
    path('artistgigapplications/<int:id>/',
         views.artist_gig_application_detail),

    path('venuegigapplications/', views.venue_gig_application_list),
    path('venuegigapplications/<int:id>/', views.venue_gig_application_detail),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
