from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MUserAddForm,MusicianAddForm
from .decorators import user_required,musician_required
from .forms import MusicianUpdateForm, UserUpdateForm, MUserUpdateForm
from .models import Musician,ProfileViews,User
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Genre_choices,Instrument_choices,Language_choices,Folder
# Genre_Choices = [gen for gen,gen1 in Genre_choices]
import os
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

def home(request):
    context = {
        'hasdp':False,
    }
    if request.user.is_authenticated:
        if request.user.is_musician:
            try:
                img_path_length = len(request.user.musician.dp.url)
                if(img_path_length>11 and request.user.musician.dp.url[img_path_length-11:]!='dummydp.png'):
                    context['hasdp']=True
            except:
                pass
        elif request.user.is_user:
            try:
                img_path_length = len(request.user.muser.dp.url)
                if(img_path_length>11 and request.user.muser.dp.url[img_path_length-11:]!='dummydp.png'):
                    context['hasdp']=True
            except:
                pass
        else:
            pass
    return render(request,'templates/home.html',context)

def UserSignup(request):
    if request.method == "POST":
        form = MUserAddForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'user'
            user.save()
            return redirect('home')
    else:
       form = MUserAddForm()
    return render(request,'User_signup.html',{'form':form})

def MusicianSignup(request):
    if request.method == "POST":
        form = MusicianAddForm(request.POST or None)
        if form.is_valid():
            musician = form.save(commit=False)
            musician.user_type = 'musician'
            musician.save()
            return redirect('home')
    else:
       form = MusicianAddForm()
    return render(request,'Musician_signup_form.html',{'form':form})


def SignInView(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #print(username)
        #print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Error wrong username/password")
    return render(request, 'login_form.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
@user_required
def ForUser(request):
    # print(request.user.is_user)
    # if request.user.is_authenticated:
    #     if request.user.is_student:
    #         return render(request,'student.html')
    #     else:
    #         return HttpResponse("Sorry")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = MUserUpdateForm(request.POST, request.FILES, instance=request.user.muser)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print("valid")
            messages.success(request, f"Your account has been updated!")
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = MUserUpdateForm(instance=request.user.muser)
    context = {
        'user':request.user,
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'user.html',context)

@login_required
@musician_required
def ForMusician(request):
    # print(request.user.is_lecturer)
    # if request.user.is_authenticated:
    #     if request.user.is_lecturer:
    #         return render(request,'teacher.html')
    #     else:
    #         return HttpResponse("Sorry")
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = MusicianUpdateForm(request.POST, request.FILES, instance=request.user.musician)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print("valid")
            messages.success(request, f"Your account has been updated!")
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = MusicianUpdateForm(instance=request.user.musician)
    context = {
        'user':request.user,
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'musician.html',context)

# @login_required
# @user_required
def ProfilePage(request,m_name):
    try:
        print("starting the process buddy!!")
        isuser = request.user.is_user
        ismus = request.user.is_musician
        isact = request.user.is_active
        issup = request.user.is_superuser
        if (isuser and isact) or issup:
            print("he is user nooooo")
            try:
                print("getting them")
                userss = User.objects.filter(is_musician=True)
                userm = userss.get(username = m_name)
                print("got it",userm,type(userm))
                context = {
                    'userm':userm,
                    'hasdp':False,
                    'hastrailersong':False,
                    'user':request.user,
                    'chatuser':True,
                    'mus_user':False,
                }
                # print(request.user)
                # # profile.views+=1
                def get_client_ip(request):
                    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                    if x_forwarded_for:
                        ip = x_forwarded_for.split(',')[0]
                    else:
                        ip = request.META.get('REMOTE_ADDR')
                    return ip
                print("finding musician now with username",userm.username)
                print("chekcing",userm.musician.user_name)
                musician = Musician.objects.get(user_name = userm.musician.user_name)
                print("and musician is found",musician)
                ProfileViews.objects.get_or_create(IPAddres=get_client_ip(request), musician=musician)
                musician.save()
                img_path_length = len(musician.dp.url)
                if(img_path_length>11 and musician.dp.url[img_path_length-11:]!='dummydp.png'):
                    context['hasdp']=True
                print(musician.dp.url[img_path_length-11:])
                if str(musician.Trailer_Song_Link)!='No link':
                    context['hastrailersong']=True
                return render(request, 'profilepage.html', context)
            except:
                raise Http404("Given username not found!!")
        if (ismus and isact) or issup:
            print("he is musician nooooooooo")
            try:
                print("getting them")
                userss = User.objects.filter(is_musician=True)
                userm = userss.get(username = m_name)
                print("got it",userm,type(userm))
                context = {
                    'userm':userm,
                    'hasdp':False,
                    'hastrailersong':False,
                    'user':request.user,
                    'chatuser':False,
                    'mus_user':True,
                }
                # print(request.user)
                # # profile.views+=1
                musician = Musician.objects.get(user_name = userm.musician.user_name)
                img_path_length = len(musician.dp.url)
                if(img_path_length>11 and musician.dp.url[img_path_length-11:]!='dummydp.png'):
                    context['hasdp']=True
                print(musician.dp.url[img_path_length-11:])
                if str(musician.Trailer_Song_Link)!='No link':
                    context['hastrailersong']=True
                print("everything is perfect no",context)
                return render(request, 'profilepage.html', context)
            except:
                raise Http404("Given username not found!!")
    except:
        print("some exception came off")
        try:
            print("getting them")
            userss = User.objects.filter(is_musician=True)
            userm = userss.get(username = m_name)
            print("got it",userm,type(userm))
            context = {
                'userm':userm,
                'hasdp':False,
                'hastrailersong':False,
                'user':request.user,
                'chatuser':False,
                'mus_user':False,
            }
            # print(request.user)
            # # profile.views+=1
            musician = Musician.objects.get(user_name = userm.musician.user_name)
            img_path_length = len(musician.dp.url)
            if(img_path_length>11 and musician.dp.url[img_path_length-11:]!='dummydp.png'):
                context['hasdp']=True
            print(musician.dp.url[img_path_length-11:])
            if str(musician.Trailer_Song_Link)!='No link':
                context['hastrailersong']=True
            return render(request, 'profilepage.html', context)
        except:
            raise Http404("Given username not found!!")



# @login_required
# @musician_required
# def ProfilePage(request,m_name):
    # try:
    #     print("getting them")
    #     userss = User.objects.filter(is_musician=True)
    #     userm = userss.get(username = m_name)
    #     print("got it",userm,type(userm))
    #     context = {
    #         'userm':userm,
    #         'hasdp':False,
    #         'hastrailersong':False,
    #         'user':request.user,
    #         'chatuser':False,
    #         'mus_user':True,
    #     }
    #     # print(request.user)
    #     # # profile.views+=1
    #     musician = Musician.objects.get(user_name = userm.musician.user_name)
    #     img_path_length = len(musician.dp.url)
    #     if(img_path_length>11 and musician.dp.url[img_path_length-11:]!='dummydp.png'):
    #         context['hasdp']=True
    #     print(musician.dp.url[img_path_length-11:])
    #     if str(musician.Trailer_Song_Link)!='No link':
    #         context['hastrailersong']=True
    #     return render(request, 'profilepage.html', context)
    # except:
    #     raise Http404("Given username not found!!")



@login_required
@user_required
def searchpage(request):
    # print(Genre_choices)
    if request.method=='POST':
        search = request.POST['srchname']
        checktoprated = request.POST.get('toprated','off')
        checkgenre = request.POST.get('genre','choose')
        checkins = request.POST.get('instruments','choose')
        checklanguage = request.POST.get('language','choose')
        # genre checks
        # checkgenre = []
        # instrumentcheck = []
        # for i,j in Genre_choices:
        #     print(i)
        #     checkgen= request.POST.get(str(i))
        #     print(checkgen)
            # if checkgen!="off":
            #     checkgenre.append(i)
        # for i,j in Instrument_choices:
        #     checkins= request.POST.get(i,'off')
        #     if checkins!="off":
        #         instrumentcheck.append(i)
        # print(checkgenre)
        # print(instrumentcheck)
        # print(search)
        context={
            "empty":True,
            'genrechoices': Genre_choices,
            'instrumentchoices':Instrument_choices,
            "Language_choices":Language_choices,
        }
        match = Musician.objects.all()
        if search and search!="":  #this is for name 
            match=match.filter(Q(user_name__icontains=search)|Q(full_name__icontains=search))
        if checktoprated=='on':
            match = match.filter(Q(top_rated=True))
        if checkgenre!='choose':
            match = match.filter(Q(Genre__contains=checkgenre))
        if checkins!='choose':
            match = match.filter(Q(Instrument__contains=checkins))
        if checklanguage!='choose':
            match = match.filter(Q(language__contains=checklanguage))
        if match :
            context["empty"]=False
            paginator = Paginator(match, 3)
            page = request.GET.get('page')
            try:
                musicianprofiles = paginator.page(page)
            except PageNotAnInteger:
                musicianprofiles = paginator.page(1)
            except EmptyPage:
                musicianprofiles = paginator.page(paginator.num_pages)
            context['page']=page
            context['musicianprofiles'] = musicianprofiles
            return render(request,'musicians.html',context)
        else:     
            # messages.error(request,'no result found')
            return render(request,'musicians.html',context)
    else:
        musicians = Musician.objects.all()
        paginator = Paginator(musicians, 3)
        page = request.GET.get('page')
        context={
            # 'musicians':musicians,
        }
        try:
            musicianprofiles = paginator.page(page)
        except PageNotAnInteger:
            musicianprofiles = paginator.page(1)
        except EmptyPage:
            musicianprofiles = paginator.page(paginator.num_pages)
        context['page']=page
        context['musicianprofiles'] = musicianprofiles
        context['genrechoices'] = Genre_choices
        context['instrumentchoices'] = Instrument_choices
        context['Language_choices'] = Language_choices
        print(context)
        return render(request,'musicians.html',context)
    
    # return render(request, 'musicians.html', context)


@login_required
@musician_required
def homedownload(request):
    return render(request ,'home_upload.html')

@login_required
@user_required
def download(request , uid):
    # print(uid)      
    # below working for permanent, trying for just preview
    # print("files in directory are ",os.listdir(f'public/static/{uid}'))
    context = {
        'uid' : uid,
        'video': False,
        'audio':False,
        'audioname':'null',
        'videoname':'null',
        'cannotview':False,
        'onlyoncecheck':False,
        'nothing':True,
    }
    folder = Folder.objects.get(uid = uid)
    # print("got that folder",folder.viewonce)
    if folder.viewsleft==0:
        context['cannotview']=True
        return render(request , 'download.html' , context)
    if folder.viewonce == True:
        context['onlyoncecheck']=True
        folder.viewsleft = 0
        folder.save()

    filename = os.listdir(f'static/{uid}')[0]
    print(filename)
    
    if filename.endswith('.mp3'):
        context["audio"] = True
        context["audioname"] = filename
        context["nothing"] = False
    elif filename.endswith('.mp4'):
        context["video"] = True
        context["videoname"] = filename
        context["nothing"] = False
    return render(request , 'download.html' , context)


class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self , request):
        try:
            data = request.data
            print("data is ",data)
            print("view only once is",data.get('viewonceonly'))
            print("type of data is",type(data))
            serializer = FileListSerializer(data = data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'files uploaded successfully',
                    'data' : serializer.data
                })
            
            return Response({
                'status' : 400,
                'message' : 'somethign went wrong',
                'data'  : serializer.errors
            })
        except Exception as e:
            print(e)
