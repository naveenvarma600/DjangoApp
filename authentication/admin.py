from django.contrib import admin
from .models import  Musician
from authentication.models import MUser, User, ProfileViews,Folder,Files,Message

admin.site.register(User)
admin.site.register(MUser)
admin.site.register(Musician)
admin.site.register(ProfileViews)
admin.site.register(Files)
admin.site.register(Folder)
admin.site.register(Message)