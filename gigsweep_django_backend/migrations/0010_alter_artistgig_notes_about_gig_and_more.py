# Generated by Django 4.2.15 on 2024-08-21 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0009_rename_description_artistgig_notes_about_gig_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistgig',
            name='notes_about_gig',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artistgig',
            name='reason_for_advertising',
            field=models.TextField(blank=True, null=True),
        ),
    ]
