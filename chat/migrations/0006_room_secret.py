# Generated by Django 3.2 on 2022-06-12 05:41

from django.db import migrations, models
import secrets


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_read_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='secret',
            field=models.CharField(default=secrets.token_hex, max_length=512),
        ),
    ]
