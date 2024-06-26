# Generated by Django 4.2.6 on 2024-06-29 01:48

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0016_remove_artistlistedgig_venue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistgigapplication',
            name='status',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Active', 'Active'), ('Transferred', 'Transferred'), ('Past', 'Past')], default=('Active',), max_length=200),
        ),
    ]
