# Generated by Django 4.1.7 on 2023-03-01 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_originalname_artwork_originaltitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='Country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.country'),
        ),
    ]
