# Generated by Django 3.2.4 on 2022-12-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_musician_trailer_song_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mailid', models.CharField(max_length=50)),
                ('phoneno', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('isuser', models.BooleanField(max_length=10)),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
    ]
