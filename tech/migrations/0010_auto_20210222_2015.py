# Generated by Django 3.1.3 on 2021-02-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0009_auto_20200804_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default='dev/images/tech.png', upload_to='tech/images/'),
        ),
    ]