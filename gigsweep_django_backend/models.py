from django.db import models
from .choices import GENRE_CHOICES, UK_COUNTRY_CHOICES, UK_COUNTY_CHOICES, ACT_TYPES, ARTIST_TYPES, GIGGING_DISTANCE, USER_TYPES, IS_APPROVED_CHOICES, STATUS_CHOICES
from multiselectfield import MultiSelectField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Artist(models.Model):

    artist_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    # Change from CharField to TextField
    bio = models.TextField(null=True)
    summary = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, null=True)
    country = models.CharField(
        max_length=50, choices=UK_COUNTRY_CHOICES, null=True)
    county = models.CharField(
        max_length=100, choices=UK_COUNTY_CHOICES, null=True)
    type_of_artist = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, null=True)
    image = models.ImageField(
        upload_to='user_profile_images/artist_profile_images/', null=True, blank=True)
    featured_artist = models.BooleanField(default=False)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    artist_membership_type = models.IntegerField(null=True)
    upcoming_gigs = models.JSONField(blank=True, null=True)
    gigging_distance = MultiSelectField(
        choices=GIGGING_DISTANCE, blank=True, max_length=200)

    def __str__(self):
        return self.artist_name


class Unavailability(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='unavailabilities')
    date = models.DateField()
    status = models.CharField(max_length=50, default="Unavailable", null=True)
    reason = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f"{self.artist} - {self.date}"


class Venue(models.Model):
    venue_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    # Change from CharField to TextField
    address = models.TextField(null=True)
    # Change from CharField to TextField
    bio = models.TextField(null=True)
    country = models.CharField(
        max_length=50, choices=UK_COUNTRY_CHOICES, null=True)
    county = models.CharField(
        max_length=100, choices=UK_COUNTY_CHOICES, null=True)
    image = models.ImageField(
        upload_to='user_profile_images/venue_profile_images/', null=True, blank=True)
    type_of_act = models.CharField(
        max_length=100, choices=ACT_TYPES, null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, null=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    venue_membership_type = models.IntegerField(null=True)

    def __str__(self):
        return self.venue_name


class ArtistListedGig(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artist_listed_gigs', null=True)
    date_of_gig = models.DateField(null=True)
    venue_name = models.CharField(max_length=100)
    country_of_venue = models.CharField(
        max_length=100, choices=UK_COUNTRY_CHOICES)
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    type_of_gig = models.CharField(max_length=50, choices=ACT_TYPES, null=True)
    type_of_artist = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    payment = models.IntegerField(null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, null=True)
    num_applications = models.PositiveIntegerField(default=0)
    # Change from CharField to TextField
    description = models.TextField(null=True)
    status = MultiSelectField(
        choices=STATUS_CHOICES, blank=True, max_length=200)

    def update_num_applications(self):
        self.num_applications = self.artists.count()

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.artist} - {self.venue_name} - {date_str}"


class VenueListedGig(models.Model):
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='venue_listed_gigs', null=True)
    date_of_gig = models.DateField(null=True)
    country_of_venue = models.CharField(
        max_length=100, choices=UK_COUNTRY_CHOICES, null=True)
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    type_of_gig = models.CharField(max_length=50, choices=ACT_TYPES, null=True)
    artist_type = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    payment = models.IntegerField(null=True)
    user_type = models.CharField(
        max_length=50, choices=USER_TYPES, null=True)
    num_applications = models.PositiveIntegerField(default=0)
    # Change from CharField to TextField
    description = models.TextField(null=True)

    def increment_num_applications(self):
        self.num_applications += 1
        self.save()

    def decrement_num_applications(self):
        self.num_applications -= 1
        self.save()

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.venue} - {date_str}"


class NewsletterSignup(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email


class MembershipOptions(models.Model):
    membership_id = models.IntegerField(null=True)
    type_of_user = models.CharField(
        max_length=50, choices=USER_TYPES, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.CharField(max_length=50, null=True)
    disclosure = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.type_of_user} - {self.title}"


class ArtistWrittenReview(models.Model):
    date_of_performance = models.DateField(null=True)
    artist_name = models.CharField(max_length=100, null=True)
    venue_name = models.CharField(max_length=100, null=True)

    # Change from CharField to TextField
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    is_approved = models.CharField(
        choices=IS_APPROVED_CHOICES, default='Under review', max_length=100, null=True)

    def __str__(self):
        return f"{self.artist_name} || {self.venue_name} || {self.date_of_performance}"


class VenueWrittenReview(models.Model):
    date_of_performance = models.DateField(null=True)
    venue_name = models.CharField(max_length=100, null=True)
    artist_name = models.CharField(max_length=100, null=True)

    # Change from CharField to TextField
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    is_approved = models.CharField(
        choices=IS_APPROVED_CHOICES, default='Under review', max_length=100, null=True)

    def __str__(self):
        return f"{self.venue_name} || {self.artist_name} || {self.date_of_performance}"


# Model only for artist listed gig applications
class ArtistGigApplication(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    artist_gig = models.ForeignKey(
        ArtistListedGig, on_delete=models.CASCADE, null=True, related_name='artists')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.artist_gig.update_num_applications()
        self.artist_gig.save()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.artist_gig.update_num_applications()
        self.artist_gig.save()

    def __str__(self):
        return f"{self.artist} applied for {self.artist_gig}"


# Model only for venue listed gig applications
class VenueGigApplication(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    venue_gig = models.ForeignKey(
        VenueListedGig, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # New application is being created
            self.venue_gig.increment_num_applications()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.venue_gig.decrement_num_applications()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.artist} applied for {self.venue_gig}"


# class ChatMessage(models.Model):
#     sender_content_type = models.ForeignKey(
#         ContentType, on_delete=models.CASCADE, related_name='sender_messages')
#     sender_object_id = models.PositiveIntegerField()
#     sender = GenericForeignKey('sender_content_type', 'sender_object_id')

#     receiver_content_type = models.ForeignKey(
#         ContentType, on_delete=models.CASCADE, related_name='receiver_messages')
#     receiver_object_id = models.PositiveIntegerField()
#     receiver = GenericForeignKey('receiver_content_type', 'receiver_object_id')

#     message = models.CharField(max_length=10000000000)
#     is_read = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['date']
#         verbose_name_plural = "Messages"

#     def __str__(self):
#         return f"{self.sender} - {self.receiver}"

#     @property
#     def sender_profile(self):
#         if isinstance(self.sender, Artist):
#             return self.sender
#         elif isinstance(self.sender, Venue):
#             return self.sender

#     @property
#     def receiver_profile(self):
#         if isinstance(self.receiver, Artist):
#             return self.receiver
#         elif isinstance(self.receiver, Venue):
#             return self.receiver
