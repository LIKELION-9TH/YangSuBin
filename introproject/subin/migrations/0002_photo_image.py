# Generated by Django 3.2.5 on 2021-07-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
