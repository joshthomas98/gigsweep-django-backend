# Generated by Django 4.2.6 on 2024-07-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0030_venuenotification_if_artist_listed_gig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venuenotification',
            old_name='if_artist_listed_gig',
            new_name='if_gig_advertised_by_artist',
        ),
        migrations.AddField(
            model_name='venuenotification',
            name='if_venue_made_gig',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
