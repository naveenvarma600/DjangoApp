# Generated by Django 3.2.4 on 2022-11-08 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_muser_birth_date_muser_city_muser_dp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='dp',
            field=models.ImageField(default='photos/dummydp.jpg', upload_to='photos/'),
        ),
    ]