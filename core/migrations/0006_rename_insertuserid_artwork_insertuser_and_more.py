# Generated by Django 4.1.7 on 2023-02-28 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_artwork_insertuserid_artwork_lastupdateuserid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='artwork',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='distributor',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='distributor',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='language',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
        migrations.RenameField(
            model_name='typeofartwork',
            old_name='InsertUserId',
            new_name='InsertUser',
        ),
        migrations.RenameField(
            model_name='typeofartwork',
            old_name='LastUpdateUserId',
            new_name='LastUpdateUser',
        ),
    ]
