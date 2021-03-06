# Generated by Django 3.2.8 on 2021-11-12 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notification_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushNotificationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('successful', 'Successful'), ('failed', 'Failed')], default='in_progress', max_length=32)),
                ('notification', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notification_app.notification')),
            ],
        ),
    ]
