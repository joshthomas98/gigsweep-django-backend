# Generated by Django 4.2.6 on 2024-01-09 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigsweep_django_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_type', models.CharField(choices=[('artist', 'Artist'), ('venue', 'Venue')], max_length=50)),
                ('receiver_id', models.PositiveIntegerField()),
                ('message', models.CharField(max_length=100000)),
                ('is_read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to='gigsweep_django_backend.artist')),
            ],
            options={
                'verbose_name_plural': 'Message',
                'ordering': ['date'],
            },
        ),
    ]