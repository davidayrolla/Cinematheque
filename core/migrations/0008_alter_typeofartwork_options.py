# Generated by Django 4.1.7 on 2023-03-01 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_country_flag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeofartwork',
            options={'verbose_name': 'type of artwork', 'verbose_name_plural': 'types of artwork'},
        ),
    ]