# Generated by Django 3.1.3 on 2021-02-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0010_auto_20210222_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=True),
        ),
    ]
