# Generated by Django 4.1.7 on 2023-03-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_userprofile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='About',
            field=models.TextField(blank=True, null=True),
        ),
    ]
