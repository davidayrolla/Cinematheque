# Generated by Django 4.1.7 on 2023-02-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_person_countryofbirth_person_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='person_photos'),
        ),
    ]