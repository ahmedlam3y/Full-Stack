# Generated by Django 2.0 on 2017-12-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20171214_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersignup',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usersignup',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersignup',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='signUp_E_mail',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
