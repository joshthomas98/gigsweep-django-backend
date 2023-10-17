from django.contrib.auth import authenticate, login
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, ArtistGigApplication, VenueGigApplication
from .serializers import ArtistSerializer, UnavailabilitySerializer, VenueSerializer, ArtistListedGigCreateSerializer, ArtistListedGigEditSerializer, VenueListedGigCreateSerializer, VenueListedGigEditSerializer, NewsletterSignupSerializer, MembershipOptionsSerializer, ArtistWrittenReviewSerializer, VenueWrittenReviewSerializer, ArtistGigApplicationSerializer, VenueGigApplicationSerializer
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
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
    email = request.data.get('email')
    password = request.data.get('password')

    artist = get_object_or_404(Artist, email=email, password=password)
    serializer = ArtistSerializer(artist)

    return Response({'id': artist.id})


# VALIDATE VENUE USER VIEW

@api_view(['POST'])
def venue_sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')

    venue = get_object_or_404(Venue, email=email, password=password)
    serializer = VenueSerializer(venue)

    return Response({'id': venue.id})


# ArtistListedGig Views

@api_view(['POST'])
def artist_listed_gig_list(request, format=None):
    serializer = ArtistListedGigCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_listed_gig_detail(request, id, format=None):
    try:
        artist_listed_gig = ArtistListedGig.objects.get(pk=id)
    except ArtistListedGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistListedGigEditSerializer(artist_listed_gig)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistListedGigEditSerializer(
            artist_listed_gig, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist_listed_gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Artist Listed Gigs By Artist View

@api_view(['GET'])
def artist_listed_gigs_by_artist(request, artist_id, format=None):
    artist = get_object_or_404(Artist, id=artist_id)
    artist_listed_gigs = artist.artist_listed_gigs.all()
    serializer = ArtistListedGigCreateSerializer(artist_listed_gigs, many=True)
    return Response(serializer.data)


# VenueListedGig Views

@api_view(['POST'])
def venue_listed_gig_list(request, format=None):
    serializer = VenueListedGigCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def venue_listed_gig_detail(request, id, format=None):
    try:
        venue_listed_gig = VenueListedGig.objects.get(pk=id)
    except VenueListedGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueListedGigEditSerializer(venue_listed_gig)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VenueListedGigEditSerializer(
            venue_listed_gig, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue_listed_gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Venue Listed Gigs By Venue View

@api_view(['GET'])
def venue_listed_gigs_by_venue(request, venue_id, format=None):
    venue = get_object_or_404(Venue, id=venue_id)
    venue_listed_gigs = venue.venue_listed_gigs.all()
    serializer = VenueListedGigCreateSerializer(venue_listed_gigs, many=True)
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

    artist_listed_gigs = ArtistListedGig.objects.filter(
        date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, payment__gte=payment)

    venue_listed_gigs = VenueListedGig.objects.filter(
        date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, payment__gte=payment)

    artist_listed_gig_serializer = ArtistListedGigEditSerializer(
        artist_listed_gigs, many=True)
    venue_listed_gig_serializer = VenueListedGigEditSerializer(
        venue_listed_gigs, many=True)

    response_data = {
        'artist_listed_gigs': artist_listed_gig_serializer.data,
        'venue_listed_gigs': venue_listed_gig_serializer.data
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

@api_view(['POST'])
def artist_gig_application_list(request, format=None):
    if request.method == 'POST':
        serializer = ArtistGigApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure that the artist_gig field is set to the corresponding gig
            # Assuming you send the gig_id in the request data
            gig_id = request.data.get('artist_gig')
            artist_gig = get_object_or_404(ArtistListedGig, id=gig_id)
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
            venue_gig = get_object_or_404(VenueListedGig, id=gig_id)
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
