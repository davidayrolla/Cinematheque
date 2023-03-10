# Generated by Django 4.1.7 on 2023-03-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_artwork_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='Distributors',
            field=models.ManyToManyField(blank=True, null=True, to='core.distributor'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='Members',
            field=models.ManyToManyField(blank=True, null=True, through='core.Membership', to='core.person'),
        ),
    ]
