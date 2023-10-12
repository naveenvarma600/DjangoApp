from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from .models import Musician,MUser
import allauth

isuser = False

class MyAccountAdapter(DefaultSocialAccountAdapter):
    
    def __init__(self, request=None):
        if(request.GET.get('checking')=="True"):
            global isuser
            isuser=True
            print(isuser)
        super(MyAccountAdapter, self).__init__()
    def new_user(self, request, sociallogin):
        return super(MyAccountAdapter, self).new_user(request,sociallogin)
    def save_user(self, request, sociallogin, form):
        global isuser
        print(isuser)
        if isuser:
            sociallogin.user.is_user=True
            user = super(MyAccountAdapter, self).save_user(request, sociallogin, form)
            student = MUser.objects.create(user=sociallogin.user,id_number=sociallogin.user.username)
            student.save()
            isuser = False
        else:
            sociallogin.user.is_musician=True
            user = super(MyAccountAdapter, self).save_user(request, sociallogin, form)
            lecturer = Musician.objects.create(user=sociallogin.user,id_number=sociallogin.user.username)
            lecturer.save()
            print("lecturer saved")
        isuser = False
        return user

    # now check whether teacher or student and add in that respective one


    
