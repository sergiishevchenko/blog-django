# Generated by Django 3.1.3 on 2020-11-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20201123_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above...', max_length=255),
        ),
    ]
