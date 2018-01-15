from django import forms


class UserRegister(forms.Form):
    Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}), label='')
    Email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    CarModel = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Car Model'}), label='')
    CarNumber = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Car Number'}), label='')
    CarColor = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Car Color'}), label='')
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='', min_length=8)
    profilePic = forms.ImageField(required=False, label="Enter Your Image")


class UserSignIn(forms.Form):
    Username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'UserName'}), label='')
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='', min_length=8)