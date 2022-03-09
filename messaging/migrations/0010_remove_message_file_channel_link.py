# Generated by Django 4.0.3 on 2022-03-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_channel_private'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file',
        ),
        migrations.AddField(
            model_name='channel',
            name='link',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
