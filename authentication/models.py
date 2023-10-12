from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.db.models.fields import CharField
from PIL import Image

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_musician = models.BooleanField(default=False)
    phone = models.CharField(max_length=60,blank=True, null=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

class MUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dp = models.ImageField(default='uphotos/dummydp.png',upload_to= "uphotos/")
    id_number = models.CharField(max_length=255)
    full_name = models.CharField(max_length=200, blank=True)
    mobile_number = CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pin_code = models.CharField(max_length=20, blank=True) 
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    full_address = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.dp.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.dp.path)
    
Genre_choices = (
    ('Pop', 'Pop'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Country', 'Country'),
    ('Folk', 'Folk'),
    ('Jazz', 'Jazz'),
    ('Classical', 'Classical'),
    ('Indie-Rock','Indie-Rock'),
    ('Ambient','Ambient')
)

Instrument_choices = (
    ('Guitar', 'Guitar'),
    ('Piano', 'Piano'),
    ('Sitar', 'Sitar'),
    ('Trumpet', 'Trumpet'),
    ('Drums', 'Drums'),
    ('Saxophone', 'Saxophone'),
    ('Vibraphone','Vibraphone'),
    ('flute','flute')
)

Language_choices = (
    ('English', 'English'),
    ('Telugu', 'Telugu'),
    ('Tamil', 'Tamil'),
    ('Hindi', 'Hindi'),
    ('Punjabi', 'Punjabi')
)

class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(default='photos/dummydp.jpg',upload_to= "photos/")
    Trailer_Song_Link = models.FileField(blank=True,upload_to="trailersongs/")
    user_name = models.CharField(max_length=200, blank=True)
    id_number = models.CharField(max_length=255)
    full_name = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    mobile_number = CharField(max_length=15, blank=True)
    Genre = MultiSelectField(choices=Genre_choices,max_choices=4,max_length=255,blank=True)
    Instrument = MultiSelectField(choices=Instrument_choices,max_choices=4,max_length=255,blank=True)
    language = MultiSelectField(choices=Language_choices,max_choices=1,max_length=255,blank=True)
    max_delivery_time = models.CharField(max_length=100, blank=True)
    Reviews = models.CharField(max_length=200, blank=True)
    Ratings = models.CharField(max_length=100, blank=True)
    top_rated = models.BooleanField(blank=True,default=False)
    birth_date = models.DateField(null=True, blank=True)
    pin_code = models.CharField(max_length=20, blank=True) 
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    full_address = models.CharField(max_length=300, blank=True)
    views = models.IntegerField(default=0, blank=True)

    def __str__(self):
        self.user_name = self.user.username
        return self.user_name

    @property
    def views_count(self):
        if(ProfileViews.objects.filter(musician=self).count()==0):
            return self.views #database is just updayed, all are removed
        self.views += abs(self.views - ProfileViews.objects.filter(musician=self).count())
        return self.views

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.dp.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.dp.path)

class ProfileViews(models.Model):
    IPAddres= models.GenericIPAddressField(default="45.243.82.169")
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)
    def __str__(self):
        return '{0} in {1} musician'.format(self.IPAddres,self.musician.user_name)


import uuid
import os
class Folder(models.Model):
    uid = models.UUIDField(primary_key= True , editable= False , default=uuid.uuid4)
    viewonce = models.BooleanField(blank=True,default=False)
    viewsleft = models.IntegerField(default=1, blank=True)
    created_at = models.DateField(auto_now= True)
 

def get_upload_path(instance , filename):
    return os.path.join(str(instance.folder.uid) , filename)


class Files(models.Model):
    folder = models.ForeignKey(Folder , on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now= True)


class Message(models.Model):
    msg_id=models.AutoField
    name=models.CharField(max_length=50)
    mailid=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=20)
    subject=models.CharField(max_length=100)
    isuser = models.BooleanField(max_length=10)
    msg=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name