# Generated by Django 5.0.6 on 2024-06-13 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
