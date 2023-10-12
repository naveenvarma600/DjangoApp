from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import User as U

from django.db import transaction

from authentication.models import MUser,Musician


class MusicianAddForm(UserCreationForm):
    address = forms.CharField(max_length=30,widget=forms.TextInput(),label="Address")
    phone = forms.CharField(max_length=30, widget=forms.TextInput(),label='Mobile No')
    firstname = forms.CharField(max_length=30,widget=forms.TextInput(),label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_musician = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        # if commit:
        #     user.save()
        # return user
        musician = Musician.objects.create(user=user, id_number=user.username)
        musician.save()
        return musician

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']


class MusicianUpdateForm(forms.ModelForm):
    full_name = forms.CharField(required=True)
    dp = forms.ImageField()
    class Meta:
        model = Musician
        fields = ["full_name","user_name","language","dp","description","Trailer_Song_Link","Genre","Instrument","max_delivery_time","Reviews","mobile_number" ,"Ratings","top_rated","birth_date","full_address","pin_code","city","state"]


class MUserAddForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(),label='Username')
    Address = forms.CharField(max_length=30, widget=forms.TextInput(), label='Address')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(), label='Mobile No')
    firstname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        muser = MUser.objects.create(user=user,id_number=user.username)
        muser.save()
        return muser

class MUserUpdateForm(forms.ModelForm):
    full_name = forms.CharField(required=True)
    dp = forms.ImageField()
    class Meta:
        model = MUser
        fields = ["full_name","dp","mobile_number" ,"birth_date","full_address","pin_code","city","state"]
