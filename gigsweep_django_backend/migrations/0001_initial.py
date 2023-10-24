# Generated by Django 4.2.6 on 2023-10-24 17:32

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('bio', models.TextField(null=True)),
                ('summary', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Country', 'Country'), ('Hip Hop', 'Hip Hop'), ('R&B', 'R&B'), ('Electronic', 'Electronic'), ('Classical', 'Classical'), ('Reggae', 'Reggae'), ('Metal', 'Metal'), ('Folk', 'Folk'), ('Blues', 'Blues'), ('World Music', 'World Music')], max_length=50, null=True)),
                ('country', models.CharField(choices=[('England', 'England'), ('Wales', 'Wales'), ('Scotland', 'Scotland'), ('Northern Ireland', 'Northern Ireland')], max_length=50, null=True)),
                ('county', models.CharField(choices=[('England', (('Bedfordshire', 'Bedfordshire'), ('Berkshire', 'Berkshire'), ('Bristol', 'Bristol'), ('Buckinghamshire', 'Buckinghamshire'), ('Cambridgeshire', 'Cambridgeshire'), ('Cheshire', 'Cheshire'), ('Cornwall', 'Cornwall'), ('Cumbria', 'Cumbria'), ('Derbyshire', 'Derbyshire'), ('Devon', 'Devon'), ('Dorset', 'Dorset'), ('Durham', 'Durham'), ('East Sussex', 'East Sussex'), ('Essex', 'Essex'), ('Gloucestershire', 'Gloucestershire'), ('Greater London', 'Greater London'), ('Greater Manchester', 'Greater Manchester'), ('Hampshire', 'Hampshire'), ('Herefordshire', 'Herefordshire'), ('Hertfordshire', 'Hertfordshire'), ('Isle of Wight', 'Isle of Wight'), ('Kent', 'Kent'), ('Lancashire', 'Lancashire'), ('Leicestershire', 'Leicestershire'), ('Lincolnshire', 'Lincolnshire'), ('Merseyside', 'Merseyside'), ('Norfolk', 'Norfolk'), ('North Yorkshire', 'North Yorkshire'), ('Northamptonshire', 'Northamptonshire'), ('Northumberland', 'Northumberland'), ('Nottinghamshire', 'Nottinghamshire'), ('Oxfordshire', 'Oxfordshire'), ('Rutland', 'Rutland'), ('Shropshire', 'Shropshire'), ('Somerset', 'Somerset'), ('South Yorkshire', 'South Yorkshire'), ('Staffordshire', 'Staffordshire'), ('Suffolk', 'Suffolk'), ('Surrey', 'Surrey'), ('Tyne and Wear', 'Tyne and Wear'), ('Warwickshire', 'Warwickshire'), ('West Midlands', 'West Midlands'), ('West Sussex', 'West Sussex'), ('West Yorkshire', 'West Yorkshire'), ('Wiltshire', 'Wiltshire'), ('Worcestershire', 'Worcestershire'))), ('Wales', (('Blaenau Gwent', 'Blaenau Gwent'), ('Bridgend', 'Bridgend'), ('Caerphilly', 'Caerphilly'), ('Cardiff', 'Cardiff'), ('Carmarthenshire', 'Carmarthenshire'), ('Ceredigion', 'Ceredigion'), ('Conwy', 'Conwy'), ('Denbighshire', 'Denbighshire'), ('Flintshire', 'Flintshire'), ('Gwynedd', 'Gwynedd'), ('Isle of Anglesey', 'Isle of Anglesey'), ('Merthyr Tydfil', 'Merthyr Tydfil'), ('Monmouthshire', 'Monmouthshire'), ('Neath Port Talbot', 'Neath Port Talbot'), ('Newport', 'Newport'), ('Pembrokeshire', 'Pembrokeshire'), ('Powys', 'Powys'), ('Rhondda Cynon Taff', 'Rhondda Cynon Taff'), ('Swansea', 'Swansea'), ('Torfaen', 'Torfaen'), ('Vale of Glamorgan', 'Vale of Glamorgan'), ('Wrexham', 'Wrexham'))), ('Scotland', (('Aberdeen City', 'Aberdeen City'), ('Aberdeenshire', 'Aberdeenshire'), ('Angus', 'Angus'), ('Argyll and Bute', 'Argyll and Bute'), ('Clackmannanshire', 'Clackmannanshire'), ('Dumfries and Galloway', 'Dumfries and Galloway'), ('Dundee City', 'Dundee City'), ('East Ayrshire', 'East Ayrshire'), ('East Dunbartonshire', 'East Dunbartonshire'), ('East Lothian', 'East Lothian'), ('East Renfrewshire', 'East Renfrewshire'), ('Edinburgh', 'Edinburgh'), ('Falkirk', 'Falkirk'), ('Fife', 'Fife'), ('Glasgow', 'Glasgow'), ('Highland', 'Highland'), ('Inverclyde', 'Inverclyde'), ('Midlothian', 'Midlothian'), ('Moray', 'Moray'), ('Na h-Eileanan Siar', 'Na h-Eileanan Siar'), ('North Ayrshire', 'North Ayrshire'), ('North Lanarkshire', 'North Lanarkshire'), ('Orkney Islands', 'Orkney Islands'), ('Perth and Kinross', 'Perth and Kinross'), ('Renfrewshire', 'Renfrewshire'), ('Scottish Borders', 'Scottish Borders'), ('Shetland Islands', 'Shetland Islands'), ('South Ayrshire', 'South Ayrshire'), ('South Lanarkshire', 'South Lanarkshire'), ('Stirling', 'Stirling'), ('West Dunbartonshire', 'West Dunbartonshire'), ('West Lothian', 'West Lothian'))), ('Northern Ireland', (('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Down', 'Down'), ('Fermanagh', 'Fermanagh'), ('Londonderry', 'Londonderry'), ('Tyrone', 'Tyrone')))], max_length=100, null=True)),
                ('type_of_artist', models.CharField(choices=[('Full band', 'Full band'), ('Solo artist', 'Solo artist'), ('Duo', 'Duo')], max_length=50, null=True)),
                ('user_type', models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_profile_images/artist_profile_images/')),
                ('featured_artist', models.BooleanField(default=False)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('artist_membership_type', models.IntegerField(null=True)),
                ('gigging_distance', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('England', (('South East', 'South East'), ('South West', 'South West'), ('London', 'London'), ('East of England', 'East of England'), ('West Midlands', 'West Midlands'), ('East Midlands', 'East Midlands'), ('Yorkshire and the Humber', 'Yorkshire and the Humber'), ('North West', 'North West'), ('North East', 'North East'))), ('Scotland', (('Highlands and Islands', 'Highlands and Islands'), ('North East Scotland', 'North East Scotland'), ('Central Belt', 'Central Belt'), ('South West Scotland', 'South West Scotland'))), ('Wales', (('North Wales', 'North Wales'), ('Mid Wales', 'Mid Wales'), ('South West Wales', 'South West Wales'), ('South East Wales', 'South East Wales'))), ('Northern Ireland', (('Antrim Coast and Glens', 'Antrim Coast and Glens'), ('Belfast', 'Belfast'), ('The Causeway Coast', 'The Causeway Coast'), ('County Armagh', 'County Armagh'), ('County Down', 'County Down'), ('Fermanagh Lakelands', 'Fermanagh Lakelands'), ('Lough Neagh', 'Lough Neagh'), ('Sperrin Mountains', 'Sperrin Mountains'), ('The Mournes', 'The Mournes'))), ('All Regions', (('Nationwide', 'Nationwide'),))], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistWrittenReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_performance', models.DateField(null=True)),
                ('artist_name', models.CharField(max_length=100, null=True)),
                ('venue_name', models.CharField(max_length=100, null=True)),
                ('review', models.TextField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('is_approved', models.CharField(choices=[('Under review', 'Under review'), ('Unapproved', 'Unapproved'), ('Approved', 'Approved')], default='Under review', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_id', models.IntegerField(null=True)),
                ('type_of_user', models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('disclosure', models.CharField(max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(null=True)),
                ('bio', models.TextField(null=True)),
                ('country', models.CharField(choices=[('England', 'England'), ('Wales', 'Wales'), ('Scotland', 'Scotland'), ('Northern Ireland', 'Northern Ireland')], max_length=50, null=True)),
                ('county', models.CharField(choices=[('England', (('Bedfordshire', 'Bedfordshire'), ('Berkshire', 'Berkshire'), ('Bristol', 'Bristol'), ('Buckinghamshire', 'Buckinghamshire'), ('Cambridgeshire', 'Cambridgeshire'), ('Cheshire', 'Cheshire'), ('Cornwall', 'Cornwall'), ('Cumbria', 'Cumbria'), ('Derbyshire', 'Derbyshire'), ('Devon', 'Devon'), ('Dorset', 'Dorset'), ('Durham', 'Durham'), ('East Sussex', 'East Sussex'), ('Essex', 'Essex'), ('Gloucestershire', 'Gloucestershire'), ('Greater London', 'Greater London'), ('Greater Manchester', 'Greater Manchester'), ('Hampshire', 'Hampshire'), ('Herefordshire', 'Herefordshire'), ('Hertfordshire', 'Hertfordshire'), ('Isle of Wight', 'Isle of Wight'), ('Kent', 'Kent'), ('Lancashire', 'Lancashire'), ('Leicestershire', 'Leicestershire'), ('Lincolnshire', 'Lincolnshire'), ('Merseyside', 'Merseyside'), ('Norfolk', 'Norfolk'), ('North Yorkshire', 'North Yorkshire'), ('Northamptonshire', 'Northamptonshire'), ('Northumberland', 'Northumberland'), ('Nottinghamshire', 'Nottinghamshire'), ('Oxfordshire', 'Oxfordshire'), ('Rutland', 'Rutland'), ('Shropshire', 'Shropshire'), ('Somerset', 'Somerset'), ('South Yorkshire', 'South Yorkshire'), ('Staffordshire', 'Staffordshire'), ('Suffolk', 'Suffolk'), ('Surrey', 'Surrey'), ('Tyne and Wear', 'Tyne and Wear'), ('Warwickshire', 'Warwickshire'), ('West Midlands', 'West Midlands'), ('West Sussex', 'West Sussex'), ('West Yorkshire', 'West Yorkshire'), ('Wiltshire', 'Wiltshire'), ('Worcestershire', 'Worcestershire'))), ('Wales', (('Blaenau Gwent', 'Blaenau Gwent'), ('Bridgend', 'Bridgend'), ('Caerphilly', 'Caerphilly'), ('Cardiff', 'Cardiff'), ('Carmarthenshire', 'Carmarthenshire'), ('Ceredigion', 'Ceredigion'), ('Conwy', 'Conwy'), ('Denbighshire', 'Denbighshire'), ('Flintshire', 'Flintshire'), ('Gwynedd', 'Gwynedd'), ('Isle of Anglesey', 'Isle of Anglesey'), ('Merthyr Tydfil', 'Merthyr Tydfil'), ('Monmouthshire', 'Monmouthshire'), ('Neath Port Talbot', 'Neath Port Talbot'), ('Newport', 'Newport'), ('Pembrokeshire', 'Pembrokeshire'), ('Powys', 'Powys'), ('Rhondda Cynon Taff', 'Rhondda Cynon Taff'), ('Swansea', 'Swansea'), ('Torfaen', 'Torfaen'), ('Vale of Glamorgan', 'Vale of Glamorgan'), ('Wrexham', 'Wrexham'))), ('Scotland', (('Aberdeen City', 'Aberdeen City'), ('Aberdeenshire', 'Aberdeenshire'), ('Angus', 'Angus'), ('Argyll and Bute', 'Argyll and Bute'), ('Clackmannanshire', 'Clackmannanshire'), ('Dumfries and Galloway', 'Dumfries and Galloway'), ('Dundee City', 'Dundee City'), ('East Ayrshire', 'East Ayrshire'), ('East Dunbartonshire', 'East Dunbartonshire'), ('East Lothian', 'East Lothian'), ('East Renfrewshire', 'East Renfrewshire'), ('Edinburgh', 'Edinburgh'), ('Falkirk', 'Falkirk'), ('Fife', 'Fife'), ('Glasgow', 'Glasgow'), ('Highland', 'Highland'), ('Inverclyde', 'Inverclyde'), ('Midlothian', 'Midlothian'), ('Moray', 'Moray'), ('Na h-Eileanan Siar', 'Na h-Eileanan Siar'), ('North Ayrshire', 'North Ayrshire'), ('North Lanarkshire', 'North Lanarkshire'), ('Orkney Islands', 'Orkney Islands'), ('Perth and Kinross', 'Perth and Kinross'), ('Renfrewshire', 'Renfrewshire'), ('Scottish Borders', 'Scottish Borders'), ('Shetland Islands', 'Shetland Islands'), ('South Ayrshire', 'South Ayrshire'), ('South Lanarkshire', 'South Lanarkshire'), ('Stirling', 'Stirling'), ('West Dunbartonshire', 'West Dunbartonshire'), ('West Lothian', 'West Lothian'))), ('Northern Ireland', (('Antrim', 'Antrim'), ('Armagh', 'Armagh'), ('Down', 'Down'), ('Fermanagh', 'Fermanagh'), ('Londonderry', 'Londonderry'), ('Tyrone', 'Tyrone')))], max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_profile_images/venue_profile_images/')),
                ('type_of_act', models.CharField(choices=[('Original Music', 'Original Music'), ('Covers', 'Covers'), ('Both', 'Both')], max_length=100, null=True)),
                ('user_type', models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube', models.CharField(blank=True, max_length=200, null=True)),
                ('venue_membership_type', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenueWrittenReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_performance', models.DateField(null=True)),
                ('venue_name', models.CharField(max_length=100, null=True)),
                ('artist_name', models.CharField(max_length=100, null=True)),
                ('review', models.TextField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('is_approved', models.CharField(choices=[('Under review', 'Under review'), ('Unapproved', 'Unapproved'), ('Approved', 'Approved')], default='Under review', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VenueListedGig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_gig', models.DateField(null=True)),
                ('country_of_venue', models.CharField(choices=[('England', 'England'), ('Wales', 'Wales'), ('Scotland', 'Scotland'), ('Northern Ireland', 'Northern Ireland')], max_length=100, null=True)),
                ('genre_of_gig', models.CharField(choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Country', 'Country'), ('Hip Hop', 'Hip Hop'), ('R&B', 'R&B'), ('Electronic', 'Electronic'), ('Classical', 'Classical'), ('Reggae', 'Reggae'), ('Metal', 'Metal'), ('Folk', 'Folk'), ('Blues', 'Blues'), ('World Music', 'World Music')], max_length=50, null=True)),
                ('type_of_gig', models.CharField(choices=[('Original Music', 'Original Music'), ('Covers', 'Covers'), ('Both', 'Both')], max_length=50, null=True)),
                ('artist_type', models.CharField(choices=[('Full band', 'Full band'), ('Solo artist', 'Solo artist'), ('Duo', 'Duo')], max_length=50, null=True)),
                ('payment', models.IntegerField(null=True)),
                ('user_type', models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True)),
                ('num_applications', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='venue_listed_gigs', to='gigsweep_django_backend.venue')),
            ],
        ),
        migrations.CreateModel(
            name='VenueGigApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gigsweep_django_backend.artist')),
                ('venue_gig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gigsweep_django_backend.venuelistedgig')),
            ],
        ),
        migrations.CreateModel(
            name='Unavailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(default='Unavailable', max_length=50, null=True)),
                ('reason', models.CharField(max_length=150, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unavailabilities', to='gigsweep_django_backend.artist')),
            ],
        ),
        migrations.CreateModel(
            name='ArtistListedGig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_gig', models.DateField(null=True)),
                ('venue_name', models.CharField(max_length=100)),
                ('country_of_venue', models.CharField(choices=[('England', 'England'), ('Wales', 'Wales'), ('Scotland', 'Scotland'), ('Northern Ireland', 'Northern Ireland')], max_length=100)),
                ('genre_of_gig', models.CharField(choices=[('Rock', 'Rock'), ('Pop', 'Pop'), ('Jazz', 'Jazz'), ('Country', 'Country'), ('Hip Hop', 'Hip Hop'), ('R&B', 'R&B'), ('Electronic', 'Electronic'), ('Classical', 'Classical'), ('Reggae', 'Reggae'), ('Metal', 'Metal'), ('Folk', 'Folk'), ('Blues', 'Blues'), ('World Music', 'World Music')], max_length=50, null=True)),
                ('type_of_gig', models.CharField(choices=[('Original Music', 'Original Music'), ('Covers', 'Covers'), ('Both', 'Both')], max_length=50, null=True)),
                ('type_of_artist', models.CharField(choices=[('Full band', 'Full band'), ('Solo artist', 'Solo artist'), ('Duo', 'Duo')], max_length=50, null=True)),
                ('payment', models.IntegerField(null=True)),
                ('user_type', models.CharField(choices=[('Artist', 'Artist'), ('Venue', 'Venue')], max_length=50, null=True)),
                ('num_applications', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(null=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist_listed_gigs', to='gigsweep_django_backend.artist')),
            ],
        ),
        migrations.CreateModel(
            name='ArtistGigApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gigsweep_django_backend.artist')),
                ('artist_gig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='gigsweep_django_backend.artistlistedgig')),
            ],
        ),
    ]
