# Generated by Django 3.0.5 on 2020-04-16 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='vody',
            new_name='body',
        ),
    ]
