# Generated by Django 3.1.3 on 2021-02-22 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20210222_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='moviepost',
        ),
    ]
