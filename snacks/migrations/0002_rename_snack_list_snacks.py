# Generated by Django 4.2.2 on 2023-06-15 00:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='snack_list',
            new_name='snacks',
        ),
    ]
