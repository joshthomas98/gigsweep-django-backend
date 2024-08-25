from django.db import models
from .choices import GENRE_CHOICES, UK_COUNTRY_CHOICES, UK_COUNTY_CHOICES, ACT_TYPES, ARTIST_TYPES, GIGGING_DISTANCE, USER_TYPES, IS_APPROVED_CHOICES, STATUS_CHOICES, VENUE_NOTIFICATION_TYPES
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, date


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


class ArtistGig(models.Model):
    original_artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='original_artist_gigs', null=True)
    current_artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='current_artist_gigs', null=True)
    previous_artists = models.ManyToManyField(
        Artist, related_name='previous_artist_gigs', blank=True)
    date_of_gig = models.DateField(null=True)
    time_of_gig = models.TimeField(null=True)
    duration_of_gig = models.PositiveIntegerField(null=True)
    venue_name = models.CharField(max_length=100, null=True)
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='gigs_at_venue', null=True, blank=True)
    country_of_venue = models.CharField(
        max_length=100, choices=UK_COUNTRY_CHOICES, null=True)
    genre_of_gig = models.CharField(
        max_length=50, choices=GENRE_CHOICES, null=True)
    type_of_gig = models.CharField(max_length=50, choices=ACT_TYPES, null=True)
    type_of_artist = models.CharField(
        max_length=50, choices=ARTIST_TYPES, null=True)
    payment = models.IntegerField(null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, null=True)
    num_applications = models.PositiveIntegerField(default=0)
    notes_about_gig = models.TextField(null=True, blank=True)
    reason_for_advertising = models.TextField(null=True, blank=True)
    status = MultiSelectField(choices=STATUS_CHOICES,
                              blank=True, max_length=200, default="Active")
    transfer_history = models.TextField(null=True, blank=True)

    # New fields
    is_advertised = models.BooleanField(default=False)
    advertised_at = models.DateTimeField(null=True, blank=True)

    def update_num_applications(self):
        self.num_applications = self.applications.count()

    def save(self, *args, **kwargs):
        # Check if the gig date is in the past
        if self.date_of_gig and self.date_of_gig < date.today():
            self.status = 'Past'

        if self.pk:  # Check if it's an update to an existing instance
            previous = ArtistGig.objects.get(pk=self.pk)
            if self.current_artist != previous.current_artist:
                # If the artist has changed, log the transfer
                self.previous_artists.add(previous.current_artist)
                transfer_record = f"Transferred from {previous.current_artist} to {self.current_artist} on {datetime.now().strftime('%Y-%m-%d')}\n"
                self.transfer_history = (
                    self.transfer_history or "") + transfer_record
                self.is_advertised = False  # Gig should no longer be advertised after transfer

        else:
            # For new instances, set the original artist as the current artist
            if not self.current_artist:
                self.current_artist = self.original_artist

        super().save(*args, **kwargs)

    def advertise(self):
        self.is_advertised = True
        self.status = 'advertised'
        self.advertised_at = timezone.now()
        self.save()

    def unadvertise(self):
        self.is_advertised = False
        self.status = 'booked'
        self.save()

    def transfer(self, new_artist):
        self.current_artist = new_artist
        self.status = 'transferred'
        self.is_advertised = False  # After transfer, it's no longer advertised
        self.save()

    def __str__(self):
        date_str = self.date_of_gig.strftime(
            '%d %b %Y') if self.date_of_gig else ''
        return f"{self.current_artist} - {self.venue_name} - {date_str}"

    @property
    def applications(self):
        return self.applications.all()  # Access related ArtistGigApplication instances

    def delete(self, *args, **kwargs):
        # Delete related notifications
        VenueNotification.objects.filter(
            if_gig_advertised_by_artist=self.id
        ).delete()
        # Call the original delete method
        super().delete(*args, **kwargs)


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
        ArtistGig, on_delete=models.CASCADE, null=True, related_name='applications')
    original_artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='original_gig_applications', null=True, blank=True)
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = MultiSelectField(
        choices=STATUS_CHOICES, blank=True, default=("Active",), max_length=200)

    def save(self, *args, **kwargs):
        # Check if the gig date has passed
        if self.artist_gig.date_of_gig and self.artist_gig.date_of_gig < timezone.now().date():
            self.status = ("Past",)  # Set status to "Past"

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


# Notification model for venues
class VenueNotification(models.Model):
    venue = models.ForeignKey(
        Venue, on_delete=models.CASCADE, related_name='notifications'
    )
    message = models.TextField()
    notification_type = MultiSelectField(
        choices=VENUE_NOTIFICATION_TYPES,
        blank=False,
        max_length=200,
        null=False,
    )
    if_gig_advertised_by_artist = models.IntegerField(null=True, blank=True)
    if_venue_made_gig = models.IntegerField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for venue {self.venue} - {self.message}"


# Notification model for artists
class ArtistNotification(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for artist {self.artist} - {self.message}"


# Contact GigSweep model
class ContactQuery(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return f"Support query from {self.name} - {self.email}"
