# Generated by Django 5.1.3 on 2024-11-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speller_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='text',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
