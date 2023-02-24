# Generated by Django 4.1.7 on 2023-02-23 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='CountryOfBirth',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='core.country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='DateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='DateOfDeath',
            field=models.DateField(blank=True, null=True),
        ),
    ]