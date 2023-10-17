from rest_framework import serializers
from django import forms
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, ArtistGigApplication, VenueGigApplication
from .choices import UK_COUNTY_CHOICES


class ArtistSerializer(serializers.ModelSerializer):
    gigging_distance = serializers.MultipleChoiceField(
        choices=UK_COUNTY_CHOICES, required=False)

    class Meta:
        model = Artist
        fields = ['id', 'artist_name', 'email', 'password', 'phone_number', 'bio', 'summary', 'genre',
                  'country', 'county', 'type_of_artist', 'user_type', 'image', 'featured_artist', 'facebook', 'twitter', 'youtube', 'artist_membership_type', 'gigging_distance']


class UnavailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Unavailability
        fields = ['id', 'artist', 'date', 'status', 'reason']


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'email', 'password', 'phone_number', 'address', 'bio',
                  'country', 'county', 'image', 'type_of_act', 'user_type', 'facebook', 'twitter', 'youtube', 'venue_membership_type']


class ArtistListedGigCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistListedGig
        fields = ['id', 'artist', 'date_of_gig', 'venue_name',
                  'country_of_venue', 'genre_of_gig', 'type_of_gig', 'type_of_artist', 'payment', 'user_type', 'num_applications']


class ArtistListedGigEditSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(
        source='artist.artist_name', read_only=True)

    class Meta:
        model = ArtistListedGig
        fields = ['id', 'artist_name', 'date_of_gig', 'venue_name',
                  'country_of_venue', 'genre_of_gig', 'type_of_gig', 'type_of_artist', 'payment', 'user_type', 'num_applications']


class VenueListedGigCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueListedGig
        fields = ['id', 'venue', 'date_of_gig', 'country_of_venue',
                  'genre_of_gig', 'type_of_gig', 'artist_type', 'payment', 'user_type', 'num_applications']


class VenueListedGigEditSerializer(serializers.ModelSerializer):
    venue_name = serializers.CharField(
        source='venue.venue_name', read_only=True)

    class Meta:
        model = VenueListedGig
        fields = ['id', 'venue_name', 'date_of_gig', 'country_of_venue',
                  'genre_of_gig', 'type_of_gig', 'artist_type', 'payment', 'user_type', 'num_applications']


class NewsletterSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsletterSignup
        fields = ['id', 'email']


class MembershipOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipOptions
        fields = ['id', 'membership_id', 'type_of_user', 'title', 'description',
                  'price', 'disclosure', 'is_active']


class ArtistWrittenReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistWrittenReview
        fields = ['id', 'date_of_performance',
                  'artist_name', 'venue_name', 'review', 'rating', 'is_approved']


class VenueWrittenReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = VenueWrittenReview
        fields = ['id', 'date_of_performance',
                  'venue_name', 'artist_name', 'review', 'rating', 'is_approved']


# class GigApplicationSerializer(serializers.ModelSerializer):

 #   class Meta:
  #      model = GigApplication
   #     fields = ['id', 'artist', 'venue', 'date_of_gig', 'email']


class ArtistGigApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistGigApplication
        fields = ['id', 'artist', 'artist_gig']


class VenueGigApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VenueGigApplication
        fields = ['id', 'artist', 'venue_gig']
