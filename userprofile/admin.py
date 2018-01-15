# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from userprofile.models import UserSignUp, UserProfile

# Register your models here.
admin.site.register(UserSignUp)
admin.site.register(UserProfile)


