from rest_framework import serializers
from django import forms
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, ArtistGigApplication, VenueGigApplication, VenueNotification, ArtistNotification
from .choices import UK_COUNTY_CHOICES


class ArtistSerializer(serializers.ModelSerializer):
    gigging_distance = serializers.MultipleChoiceField(
        choices=UK_COUNTY_CHOICES, required=False)

    class Meta:
        model = Artist
        fields = ['id', 'artist_name', 'email', 'password', 'phone_number', 'bio', 'summary', 'genre',
                  'country', 'county', 'type_of_artist', 'user_type', 'image', 'featured_artist', 'facebook', 'twitter', 'youtube', 'artist_membership_type', 'upcoming_gigs', 'gigging_distance']


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
        fields = ['id', 'artist', 'date_of_gig', 'venue_name', 'venue', 'country_of_venue', 'genre_of_gig',
                  'type_of_gig', 'type_of_artist', 'payment', 'user_type', 'num_applications', 'description', 'status']


class ArtistListedGigEditSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(
        source='artist.artist_name', read_only=True)
    artist_id = serializers.IntegerField(source='artist.id', read_only=True)
    venue_id = serializers.IntegerField(source='venue.id', read_only=True)

    class Meta:
        model = ArtistListedGig
        fields = ['id', 'artist_name', 'artist_id', 'date_of_gig', 'venue_name', 'venue_id',
                  'country_of_venue', 'genre_of_gig', 'type_of_gig', 'type_of_artist',
                  'payment', 'user_type', 'num_applications', 'description', 'status']


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
        fields = ['id', 'artist', 'artist_gig',
                  'original_artist', 'venue', 'message', 'status']


class VenueGigApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VenueGigApplication
        fields = ['id', 'artist', 'venue_gig']


# class ChatMessageSerializer(serializers.ModelSerializer):
#     sender_profile = serializers.SerializerMethodField()
#     receiver_profile = serializers.SerializerMethodField()

#     class Meta:
#         model = ChatMessage
#         fields = ['id', 'sender_content_type', 'sender_object_id', 'sender_profile',
#                   'receiver_content_type', 'receiver_object_id', 'receiver_profile',
#                   'message', 'is_read', 'date']

#     def get_sender_profile(self, obj):
#         if obj.sender_content_type.model == 'artist':
#             artist = Artist.objects.get(id=obj.sender_object_id)
#             return ArtistSerializer(artist).data
#         elif obj.sender_content_type.model == 'venue':
#             venue = Venue.objects.get(id=obj.sender_object_id)
#             return VenueSerializer(venue).data

#     def get_receiver_profile(self, obj):
#         if obj.receiver_content_type.model == 'artist':
#             artist = Artist.objects.get(id=obj.receiver_object_id)
#             return ArtistSerializer(artist).data
#         elif obj.receiver_content_type.model == 'venue':
#             venue = Venue.objects.get(id=obj.receiver_object_id)
#             return VenueSerializer(venue).data


class VenueNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueNotification
        fields = ['id', 'venue', 'message',
                  'notification_type', 'if_gig_advertised_by_artist', 'if_venue_made_gig', 'is_read', 'created_at']
        read_only_fields = ['created_at']


class ArtistNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistNotification
        fields = ['id', 'artist', 'message', 'is_read', 'created_at']
        read_only_fields = ['created_at']
