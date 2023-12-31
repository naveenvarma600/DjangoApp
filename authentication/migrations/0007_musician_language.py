# Generated by Django 3.2.4 on 2022-11-14 15:58

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_musician_dp'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='language',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('English', 'English'), ('Telugu', 'Telugu'), ('Tamil', 'Tamil'), ('Hindi', 'Hindi'), ('Punjabi', 'Punjabi')], max_length=255),
        ),
    ]
