# Generated by Django 4.1.7 on 2023-02-23 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_country_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='Flag',
            field=models.ImageField(blank=True, null=True, upload_to='countries_flags'),
        ),
    ]
