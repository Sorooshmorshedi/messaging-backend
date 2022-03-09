# Generated by Django 4.0.3 on 2022-03-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_channel_group_message_seen_like_archived_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='store_image/'),
        ),
        migrations.AddField(
            model_name='message',
            name='pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='store_image/'),
        ),
    ]
