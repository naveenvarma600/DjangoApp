from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.decorators import musician_required
# Create your views here.
from chat.models import Thread
from authentication.models import User
from .models import Thread

@login_required
def messages_page(request):
    if request.method=='POST':
        print("from user name is",request.user.username)
        mid = request.POST.get('mname','defaultvalue')
        print("to username is",mid)
        userid = User.objects.get(username = request.user.username)
        musicianid = User.objects.get(username = mid)
        print(userid,musicianid)
        Thread.objects.get_or_create(first_person = userid,second_person = musicianid)
        pass
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)

@login_required
@musician_required
def uploadmusic(request):
    if request.method=='POST':
        print("from user name is",request.user.username)
        checkviewonce = request.POST.get('view_once','off')
        print("check view once",checkviewonce)
        # chatFileUpload
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'messages.html', context)

