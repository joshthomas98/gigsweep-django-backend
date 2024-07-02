# Generated by Django 4.2.6 on 2024-06-29 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0014_alter_artistgigapplication_artist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistlistedgig',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gigs', to='gigsweep_django_backend.venue'),
        ),
    ]