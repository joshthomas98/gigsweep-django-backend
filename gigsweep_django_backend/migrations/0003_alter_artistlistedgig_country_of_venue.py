# Generated by Django 4.2.15 on 2024-08-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0002_artistgigapplication_applied_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistlistedgig',
            name='country_of_venue',
            field=models.CharField(choices=[('England', 'England'), ('Wales', 'Wales'), ('Scotland', 'Scotland'), ('Northern Ireland', 'Northern Ireland')], max_length=100, null=True),
        ),
    ]