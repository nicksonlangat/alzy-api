# Generated by Django 3.1.6 on 2021-02-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]