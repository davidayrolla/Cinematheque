# Generated by Django 4.1.7 on 2023-03-01 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_typeofartwork_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeofartwork',
            options={'verbose_name': 'Type of Artwork', 'verbose_name_plural': 'Types of Artwork'},
        ),
    ]
