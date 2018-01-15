# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from userprofile import models
from userprofile import forms
import sqlite3

# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    register_data = forms.UserRegister(request.POST or None)
    signIn_data = forms.UserSignIn(request.POST or None)
    newuser = models.UserSignUp()
    if register_data.is_valid():
        newuser.signUp_name = register_data.cleaned_data['Name']
        newuser.signUp_E_mail = register_data.cleaned_data['Email']
        newuser.signUp_Car_model = register_data.cleaned_data['CarModel']
        newuser.signUp_Car_number = register_data.cleaned_data['CarNumber']
        newuser.signUp_Car_color = register_data.cleaned_data['CarColor']
        newuser.signUp_Password = register_data.cleaned_data['password']
        newuser.profile_pic = register_data.cleaned_data['profilePic']
        newuser.save()
    if signIn_data.is_valid():
        username = signIn_data.cleaned_data['Username']
        password = signIn_data.cleaned_data['password']
        conn = sqlite3.connect('db.sqlite3')
        conn.row_factory = sqlite3.Row
        cursor = conn.execute("select * from userprofile_usersignup")
        for row in cursor:
            if row['signUp_name'] == username and row['signUp_Password'] == password:
                print('Logged in')
                activities = models.UserProfile.objects.all()
                context = {
                    'activities': activities,
                    'username': row['signUp_name'],
                    'carNumber': row['signUp_Car_number'],
                    'carModel': row['signUp_Car_model'],
                    'carColor': row['signUp_Car_color'],
                }

                return render(request, 'profile.html', context)
    context = {
        'register_data': register_data,
        'signIn': signIn_data
    }

    return render(request, 'register.html', context)



def profile(request):
    user = models.UserProfile.objects.all()
    context = {
        'user': user
    }

    return render(request, 'profile.html', context)


def entercar(request):
    return render(request, 'entercar.html')


def outcar(request):
    return render(request, 'OutCar.html')

