# Generated by Django 5.1.3 on 2024-11-27 16:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speller_app', '0002_rename_user_id_text_user_alter_text_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Text',
            new_name='Report',
        ),
    ]
