# Generated by Django 4.1.7 on 2023-03-10 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_userprofile_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'verbose_name': 'Membership', 'verbose_name_plural': 'Memberships'},
        ),
        migrations.AlterField(
            model_name='membership',
            name='Role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.role'),
        ),
    ]
