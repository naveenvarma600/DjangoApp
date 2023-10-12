from django.shortcuts import render,redirect
from authentication.models import Message

def about(request):
    params = {"key1":"value1"}
    return render(request,"about.html",params)


def contact(request):
    context = {

    }
    context['isuser']=True
    if str(request.user)=="AnonymousUser":
        context['isuser']=False
    if request.method == "POST":
        name = request.POST["txt_name"]
        mailid = request.POST["txt_email"]
        phoneno = request.POST["txt_phone"]
        subject = request.POST["txt_subject"]
        msg = request.POST["txt_message"]
        isuser = False
        if request.user.is_user:
            isuser = True
        msgb = Message(name=name,mailid = mailid,phoneno = phoneno,subject = subject,isuser = isuser,msg = msg)
        msgb.save()
        return redirect('/')
    return render(request,"contact.html",context)