# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class UserSignUp(models.Model):
    signUp_name = models.CharField(max_length=150)
    signUp_E_mail = models.CharField(max_length=40, unique=True)
    signUp_Car_model = models.CharField(max_length=150)
    signUp_Car_number = models.CharField(max_length=150)
    signUp_Car_color = models.CharField(max_length=150)
    signUp_Password = models.CharField(max_length=256)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)


class UserProfile(models.Model):
    user_ID = models.ForeignKey(UserSignUp,on_delete=models.CASCADE)
    enter_Date = models.DateTimeField()
    out_Date = models.DateTimeField()
    cost = models.CharField(max_length=64)




