# Generated by Django 4.2.2 on 2023-06-21 21:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0002_rename_snack_list_snacks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='snacks',
            new_name='Snack',
        ),
    ]
