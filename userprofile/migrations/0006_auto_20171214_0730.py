# Generated by Django 2.0 on 2017-12-14 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.UserSignUp'),
        ),
    ]
