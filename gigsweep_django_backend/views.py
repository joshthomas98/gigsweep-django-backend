from django.contrib.auth import authenticate, login
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Artist, Unavailability, Venue, ArtistGig, VenueGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, ArtistGigApplication, VenueGigApplication, VenueNotification, ArtistNotification, ContactQuery
from .serializers import ArtistSerializer, UnavailabilitySerializer, VenueSerializer, ArtistGigCreateSerializer, ArtistGigEditSerializer, VenueGigCreateSerializer, VenueGigEditSerializer, NewsletterSignupSerializer, MembershipOptionsSerializer, ArtistWrittenReviewSerializer, VenueWrittenReviewSerializer, ArtistGigApplicationSerializer, VenueGigApplicationSerializer, VenueNotificationSerializer, ArtistNotificationSerializer, ContactQuerySerializer
from django.db.models import Q
from django.utils import timezone
import json


# Artist View

@api_view(['GET', 'POST'])
def artist_list(request, format=None):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            artist = serializer.save()
            return Response({'id': artist.id, **serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, id, format=None):

    try:
        artist = Artist.objects.get(pk=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_artists(request, format=None):
    """
    Create multiple Artist objects in one go with a list of JSON data.
    """
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Unavailability View

@api_view(['GET', 'POST'])
def unavailability_list(request, format=None):

    if request.method == 'GET':
        unavailabilities = Unavailability.objects.all()
        serializer = UnavailabilitySerializer(unavailabilities, many=True)

        # Convert dates to the desired timezone
        for item in serializer.data:
            item['date'] = timezone.localtime(item['date']).date()

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnavailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def unavailability_detail(request, id, format=None):

    try:
        unavailability = Unavailability.objects.filter(artist_id=id)
    except Unavailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UnavailabilitySerializer(unavailability, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UnavailabilitySerializer(
            unavailability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        unavailability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Venue View

@api_view(['GET', 'POST'])
def venue_list(request, format=None):

    if request.method == 'GET':
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def venue_detail(request, id, format=None):

    try:
        venue = Venue.objects.get(pk=id)
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueSerializer(venue)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VenueSerializer(venue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VALIDATE ARTIST USER VIEW

@api_view(['POST'])
def artist_sign_in(request):
    email = request.data.get('email').lower()
    password = request.data.get('password')

    try:
        artist = Artist.objects.get(email__iexact=email, password=password)
    except Artist.DoesNotExist:
        return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artist)
    return Response({'id': artist.id})


# VALIDATE VENUE USER VIEW

@api_view(['POST'])
def venue_sign_in(request):
    # Convert entered email to lowercase
    email = request.data.get('email').lower()
    password = request.data.get('password')

    try:
        # Case-insensitive email comparison
        venue = Venue.objects.get(email__iexact=email, password=password)
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = VenueSerializer(venue)
    return Response({'id': venue.id})


# ArtistGig Views

def notify_venue_on_gig_advertisement(gig):
    """Notify the venue when an artist advertises a gig."""
    if gig.venue:
        message = f"The artist {gig.current_artist.artist_name} has advertised their gig on {gig.date_of_gig}."
        VenueNotification.objects.create(
            venue=gig.venue,
            message=message,
            notification_type=["GIG_TRANSFER"],
            if_gig_advertised_by_artist=gig.id  # Store the gig ID
        )


@api_view(['POST'])
def artist_gig_list(request, format=None):
    serializer = ArtistGigCreateSerializer(data=request.data)
    if serializer.is_valid():
        gig = serializer.save()
        if gig.is_advertised:  # Check if the gig is advertised
            notify_venue_on_gig_advertisement(gig)  # Notify the venue
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_gig_detail(request, id, format=None):
    try:
        artist_gig = ArtistGig.objects.get(pk=id)
    except ArtistGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistGigEditSerializer(artist_gig)
        return Response(serializer.data)

    elif request.method == 'PUT':
        original_is_advertised = artist_gig.is_advertised
        serializer = ArtistGigEditSerializer(
            artist_gig, data=request.data, partial=True)

        if serializer.is_valid():
            updated_gig = serializer.save()

            # Notify venue if gig was not advertised before but is now advertised
            if not original_is_advertised and updated_gig.is_advertised:
                notify_venue_on_gig_advertisement(updated_gig)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist_gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def artist_gig_applications(request, gig_id):
    try:
        artist_gig = ArtistGig.objects.get(pk=gig_id)
    except ArtistGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    applications = ArtistGigApplication.objects.filter(artist_gig=artist_gig)
    serializer = ArtistGigApplicationSerializer(applications, many=True)
    return Response(serializer.data)


# Artist Gigs By Artist View

@api_view(['GET'])
def artist_gigs_by_artist(request, artist_id, format=None):
    artist = get_object_or_404(Artist, id=artist_id)
    artist_gigs = artist.current_artist_gigs.all()
    serializer = ArtistGigCreateSerializer(artist_gigs, many=True)
    return Response(serializer.data)


# VenueGig Views

@api_view(['POST'])
def venue_gig_list(request, format=None):
    """
    Handle POST request to create a new VenueGig.
    """
    serializer = VenueGigCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, Update or Delete a specific Venue Gig
@api_view(['GET', 'PUT', 'DELETE'])
def venue_gig_detail(request, id, format=None):
    """
    Handle GET, PUT, DELETE requests for a specific VenueGig.
    """
    try:
        venue_gig = VenueGig.objects.get(pk=id)
    except VenueGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve details of a specific VenueGig
        serializer = VenueGigEditSerializer(venue_gig)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update details of a specific VenueGig
        serializer = VenueGigEditSerializer(venue_gig, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete a specific VenueGig
        venue_gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# List all Venue Gigs for a specific Venue
@api_view(['GET'])
def venue_gigs_by_venue(request, venue_id, format=None):
    """
    Handle GET request to retrieve all VenueGigs for a specific Venue.
    """
    venue = get_object_or_404(Venue, id=venue_id)
    venue_gigs = venue.venue_gigs.all()  # Assuming the related_name is 'venue_gigs'
    serializer = VenueGigCreateSerializer(venue_gigs, many=True)
    return Response(serializer.data)


# SEARCH FOR ARTISTS VIEW

@api_view(['POST'])
def artist_search(request):

    date_of_gig = request.data.get('date_of_gig')
    genre = request.data.get('genre')
    type_of_artist = request.data.get('type_of_artist')
    country = request.data.get('country')

    result = list(Artist.objects.filter(
        ~Q(unavailabilities__date=date_of_gig),
        genre=genre,
        type_of_artist=type_of_artist,
        country=country
    ).values())

    json_result = json.dumps(result)

    return Response(result)


# NewsletterSignup View

@api_view(['GET', 'POST'])
def newsletter_signup_list(request, format=None):

    if request.method == 'GET':
        newsletter_signups = NewsletterSignup.objects.all()
        serializer = NewsletterSignupSerializer(newsletter_signups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsletterSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def newsletter_signup_detail(request, id, format=None):

    try:
        newsletter_signup = NewsletterSignup.objects.get(pk=id)
    except NewsletterSignup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewsletterSignupSerializer(newsletter_signup)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsletterSignupSerializer(
            newsletter_signup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        newsletter_signup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Featured Artist View

@api_view(['GET'])
def featured_artist_list(request, format=None):
    featured_artist = Artist.objects.filter(featured_artist=True)
    serializer = ArtistSerializer(featured_artist, many=True)
    return Response(serializer.data)


# Membership Options View

@api_view(['GET', 'POST'])
def membership_option_list(request, format=None):

    if request.method == 'GET':
        membership_options = MembershipOptions.objects.all()
        serializer = MembershipOptionsSerializer(membership_options, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MembershipOptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def membership_option_detail(request, id, format=None):

    try:
        membership_option = MembershipOptions.objects.get(pk=id)
    except MembershipOptions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MembershipOptionsSerializer(membership_option)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MembershipOptionsSerializer(
            membership_option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        membership_option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # Artist Listed Gig Search View

# @api_view(['POST'])
# def artist_listed_gig_search(request):

#     date_of_gig = request.data.get('date_of_gig')
#     country_of_venue = request.data.get('country_of_venue')
#     genre_of_gig = request.data.get('genre_of_gig')
#     type_of_gig = request.data.get('type_of_gig')
#     artist_type = request.data.get('artist_type')
#     payment = request.data.get('payment')

#     result = ArtistListedGig.objects.filter(
#         date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, artist_type=artist_type, payment=payment)
#     serializer = ArtistListedGigSerializer(result, many=True)
#     return Response(serializer.data)


# # Venue Listed Gig Search View

# @api_view(['POST'])
# def venue_listed_gig_search(request):

#     date_of_gig = request.data.get('date_of_gig')
#     country_of_venue = request.data.get('country_of_venue')
#     genre_of_gig = request.data.get('genre_of_gig')
#     type_of_gig = request.data.get('type_of_gig')
#     artist_type = request.data.get('artist_type')
#     payment = request.data.get('payment')

#     result = VenueListedGig.objects.filter(
#         date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, artist_type=artist_type, payment=payment)
#     serializer = VenueListedGigSerializer(result, many=True)
#     return Response(serializer.data)


# Gig Search View

@api_view(['POST'])
def gig_search(request):
    date_of_gig = request.data.get('date_of_gig')
    country_of_venue = request.data.get('country_of_venue')
    genre_of_gig = request.data.get('genre_of_gig')
    type_of_gig = request.data.get('type_of_gig')
    payment = request.data.get('payment')

    # Filter ArtistGigs with additional condition of is_advertised=True
    artist_gigs = ArtistGig.objects.filter(
        date_of_gig=date_of_gig,
        country_of_venue=country_of_venue,
        genre_of_gig=genre_of_gig,
        type_of_gig=type_of_gig,
        payment__gte=payment,
        is_advertised=True  # Only return gigs that are advertised
    )

    # Filter VenueGigs as usual
    venue_gigs = VenueGig.objects.filter(
        date_of_gig=date_of_gig,
        country_of_venue=country_of_venue,
        genre_of_gig=genre_of_gig,
        type_of_gig=type_of_gig,
        payment__gte=payment
    )

    artist_gig_serializer = ArtistGigEditSerializer(artist_gigs, many=True)
    venue_gig_serializer = VenueGigEditSerializer(
        venue_gigs, many=True)

    response_data = {
        'artist_gigs': artist_gig_serializer.data,
        'venue_gigs': venue_gig_serializer.data
    }

    return Response(response_data)


# Artist Written Review View

@api_view(['GET', 'POST'])
def artist_written_review_list(request, format=None):

    if request.method == 'GET':
        artist_written_reviews = ArtistWrittenReview.objects.all()
        serializer = ArtistWrittenReviewSerializer(
            artist_written_reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistWrittenReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_written_review_detail(request, id, format=None):

    try:
        artist_written_review = ArtistWrittenReview.objects.get(pk=id)
    except ArtistWrittenReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistWrittenReviewSerializer(artist_written_review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistWrittenReviewSerializer(
            artist_written_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist_written_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Venue Written Review View

@api_view(['GET', 'POST'])
def venue_written_review_list(request, format=None):

    if request.method == 'GET':
        venue_written_reviews = VenueWrittenReview.objects.all()
        serializer = VenueWrittenReviewSerializer(
            venue_written_reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VenueWrittenReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def venue_written_review_detail(request, id, format=None):

    try:
        venue_written_review = VenueWrittenReview.objects.get(pk=id)
    except VenueWrittenReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueWrittenReviewSerializer(venue_written_review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VenueWrittenReviewSerializer(
            venue_written_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue_written_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Artist Written Review Profanity Check View

@csrf_exempt
def artist_written_review_check_profanities(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Extract the fields from the JSON data
            date_of_performance = data.get('date_of_performance')
            artist_name = data.get('artist_name')
            venue_name = data.get('venue_name')
            review_text = data.get('review')
            rating = data.get('rating')

            # Save the review in the ArtistWrittenReview model
            review = ArtistWrittenReview(
                date_of_performance=date_of_performance,
                artist_name=artist_name,
                venue_name=venue_name,
                review=review_text,
                rating=rating
            )
            review.save()

            # Call Perspective API to check for profanities
            api_key = 'AIzaSyDEIjE6t5zbfmSljgi5jrDRhcfM0yjg-NU'
            endpoint = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=' + api_key

            perspective_data = {
                'comment': {
                    'text': review_text
                },
                'requestedAttributes': {
                    'TOXICITY': {}
                }
            }

            response = requests.post(endpoint, json=perspective_data)
            if response.status_code == 200:
                perspective_result = response.json()
                toxicity_score = perspective_result['attributeScores']['TOXICITY']['summaryScore']['value']

                # Update the is_approved field based on profanity check
                review.is_approved = 'Unapproved' if toxicity_score >= 0.5 else 'Approved'
                review.save()

                # Serialize the review data
                serializer = ArtistWrittenReviewSerializer(review)

                # Return the serialized review data as JSON response
                return JsonResponse(serializer.data)

            else:
                # Handle the error case appropriately
                return JsonResponse({'error': 'Error occurred while checking for profanities.'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'})


# Venue Written Review Profanity Check View

@csrf_exempt
def venue_written_review_check_profanities(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Extract the fields from the JSON data
            date_of_performance = data.get('date_of_performance')
            venue_name = data.get('venue_name')
            artist_name = data.get('artist_name')
            review_text = data.get('review')
            rating = data.get('rating')

            # Save the review in the ArtistWrittenReview model
            review = VenueWrittenReview(
                date_of_performance=date_of_performance,
                venue_name=venue_name,
                artist_name=artist_name,
                review=review_text,
                rating=rating
            )
            review.save()

            # Call Perspective API to check for profanities
            api_key = 'AIzaSyDEIjE6t5zbfmSljgi5jrDRhcfM0yjg-NU'
            endpoint = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key=' + api_key

            perspective_data = {
                'comment': {
                    'text': review_text
                },
                'requestedAttributes': {
                    'TOXICITY': {}
                }
            }

            response = requests.post(endpoint, json=perspective_data)
            if response.status_code == 200:
                perspective_result = response.json()
                toxicity_score = perspective_result['attributeScores']['TOXICITY']['summaryScore']['value']

                # Update the is_approved field based on profanity check
                review.is_approved = 'Unapproved' if toxicity_score >= 0.5 else 'Approved'
                review.save()

                # Serialize the review data
                serializer = VenueWrittenReviewSerializer(review)

                # Return the serialized review data as JSON response
                return JsonResponse(serializer.data)

            else:
                # Handle the error case appropriately
                return JsonResponse({'error': 'Error occurred while checking for profanities.'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'})


# SEARCH BAR PROFILE SEARCH

@api_view(['GET'])
def search_bar_artists(request):
    query = request.GET.get('q', '')
    artists = Artist.objects.filter(artist_name__icontains=query)
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_bar_venues(request):
    query = request.GET.get('q', '')
    venues = Venue.objects.filter(venue_name__icontains=query)
    serializer = VenueSerializer(venues, many=True)
    return Response(serializer.data)


# Artist Gig Application View

@api_view(['GET', 'POST'])
def artist_gig_application_list(request, format=None):
    if request.method == 'GET':
        venue_id = request.query_params.get('venue_id')
        if venue_id:
            applications = ArtistGigApplication.objects.filter(
                venue__id=venue_id)
        else:
            applications = ArtistGigApplication.objects.all()
        serializer = ArtistGigApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistGigApplicationSerializer(data=request.data)
        if serializer.is_valid():
            gig_id = request.data.get('artist_gig')
            artist_gig = get_object_or_404(ArtistGig, id=gig_id)
            serializer.save(artist_gig=artist_gig)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_gig_application_detail(request, id, format=None):
    try:
        artist_gig_application = ArtistGigApplication.objects.get(pk=id)
    except ArtistGigApplication.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistGigApplicationSerializer(artist_gig_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistGigApplicationSerializer(
            artist_gig_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist_gig_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Venue Gig Application View

@api_view(['POST'])
def venue_gig_application_list(request, format=None):
    if request.method == 'POST':
        serializer = VenueGigApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure that the venue_gig field is set to the corresponding gig
            # Assuming you send the gig_id in the request data
            gig_id = request.data.get('venue_gig')
            venue_gig = get_object_or_404(VenueGig, id=gig_id)
            serializer.save(venue_gig=venue_gig)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def venue_gig_application_detail(request, id, format=None):

    try:
        venue_gig_application = VenueGigApplication.objects.get(pk=id)
    except VenueGigApplication.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueGigApplicationSerializer(venue_gig_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VenueGigApplicationSerializer(
            venue_gig_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue_gig_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class SendMessageView(generics.CreateAPIView):
#     serializer_class = ChatMessageSerializer

#     def perform_create(self, serializer):
#         # Set the sender and receiver based on your logic
#         sender_id = self.request.data.get('sender_object_id')
#         receiver_id = self.request.data.get('receiver_object_id')

#         sender_content_type = self.request.data.get('sender_content_type')
#         receiver_content_type = self.request.data.get('receiver_content_type')

#         sender = self.get_object(sender_id, sender_content_type)
#         receiver = self.get_object(receiver_id, receiver_content_type)

#         serializer.save(sender=sender, receiver=receiver)

#     def get_object(self, object_id, content_type):
#         model_class = None
#         if content_type == 'artist':
#             model_class = Artist
#         elif content_type == 'venue':
#             model_class = Venue

#         if model_class:
#             return model_class.objects.get(id=object_id)
#         return None


# class ChatMessageListView(generics.ListAPIView):
#     serializer_class = ChatMessageSerializer

#     def get_queryset(self):
#         # Set the user (sender or receiver) based on your authentication logic
#         user_id = self.request.user.id

#         queryset = ChatMessage.objects.filter(
#             sender_object_id=user_id) | ChatMessage.objects.filter(receiver_object_id=user_id)
#         return queryset


# Functions for notification functionality

# Venue notifications

# Fetch notifications for a specific venue
@api_view(['GET'])
def venue_notifications(request, venue_id):
    try:
        notifications = VenueNotification.objects.filter(venue_id=venue_id)
        serializer = VenueNotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except VenueNotification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Contact GigSweep

@api_view(['GET', 'POST'])
def contact_query_list(request, format=None):
    if request.method == 'GET':
        contact_queries = ContactQuery.objects.all()
        serializer = ContactQuerySerializer(
            contact_queries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactQuerySerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.save()
            return Response({'id': query.id, **serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_query_detail(request, id, format=None):

    try:
        query = ContactQuery.objects.get(pk=id)
    except ContactQuery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactQuerySerializer(query)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactQuerySerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
