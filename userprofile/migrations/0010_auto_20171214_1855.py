# Generated by Django 2.0 on 2017-12-14 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_auto_20171214_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersignup',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usersignup',
            name='password',
        ),
    ]