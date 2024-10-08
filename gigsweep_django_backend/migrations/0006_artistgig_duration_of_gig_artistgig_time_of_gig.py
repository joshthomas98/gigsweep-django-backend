# Generated by Django 4.2.15 on 2024-08-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0005_artistgig_advertised_at_artistgig_is_advertised'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistgig',
            name='duration_of_gig',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='artistgig',
            name='time_of_gig',
            field=models.TimeField(null=True),
        ),
    ]
