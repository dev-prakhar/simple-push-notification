# Generated by Django 3.2.8 on 2021-11-03 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0002_pushnotificationrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pushnotificationrequest',
            old_name='notification_id',
            new_name='notification',
        ),
    ]
