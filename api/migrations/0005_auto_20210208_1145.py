# Generated by Django 3.1.6 on 2021-02-08 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_file_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file',
            new_name='image',
        ),
    ]