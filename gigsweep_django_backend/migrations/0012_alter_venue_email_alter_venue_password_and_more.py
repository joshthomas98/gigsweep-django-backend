# Generated by Django 4.2.6 on 2024-03-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0011_alter_artist_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
