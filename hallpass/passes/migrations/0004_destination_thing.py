# Generated by Django 4.2.4 on 2023-08-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0003_remove_destination_thing'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='thing',
            field=models.CharField(default='', max_length=200),
        ),
    ]
