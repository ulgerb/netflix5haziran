# Generated by Django 4.2 on 2024-01-12 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermy',
            name='packed',
        ),
    ]
