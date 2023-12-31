# Generated by Django 4.1.2 on 2022-11-06 13:13

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="musician",
            name="Genre",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("Pop", "Pop"),
                    ("Hip-Hop", "Hip-Hop"),
                    ("Country", "Country"),
                    ("Folk", "Folk"),
                    ("Jazz", "Jazz"),
                    ("Classical", "Classical"),
                    ("Indie-Rock", "Indie-Rock"),
                    ("Ambient", "Ambient"),
                ],
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="musician",
            name="Instrument",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("Guitar", "Guitar"),
                    ("Piano", "Piano"),
                    ("Sitar", "Sitar"),
                    ("Trumpet", "Trumpet"),
                    ("Drums", "Drums"),
                    ("Saxophone", "Saxophone"),
                    ("Vibraphone", "Vibraphone"),
                    ("flute", "flute"),
                ],
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="musician",
            name="Ratings",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="musician",
            name="Reviews",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="musician",
            name="Trailer_Song_Link",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="musician",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="musician",
            name="city",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="musician",
            name="description",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="musician",
            name="dp",
            field=models.ImageField(default="photos/dummydp.png", upload_to="photos/"),
        ),
        migrations.AddField(
            model_name="musician",
            name="full_address",
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="musician",
            name="full_name",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="musician",
            name="max_delivery_time",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="musician",
            name="mobile_number",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name="musician",
            name="pin_code",
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name="musician",
            name="state",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="musician",
            name="top_rated",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
