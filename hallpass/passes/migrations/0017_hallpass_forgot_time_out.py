# Generated by Django 4.2.5 on 2023-09-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0016_remove_hallpass_cancel_time_alter_hallpass_time_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallpass',
            name='forgot_time_out',
            field=models.BooleanField(default=False),
        ),
    ]