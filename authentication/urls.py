from django.urls import path,include

from authentication import views


urlpatterns = [
    path('',views.home,name='home'),
    path('user/signup/',views.UserSignup, name = 'UserSignup'),
    path('musician/signup/',views.MusicianSignup, name = 'MusicianSignup'),

    path('login/',views.SignInView,name = 'login'),
    path('logout/',views.logout_view,name = 'logout'),

    path('foruser/',views.ForUser,name='ForUser'),
    path('formusician/',views.ForMusician,name='ForMusician'),
    path('accounts/', include('allauth.urls')),
    path('musicians/<str:m_name>',views.ProfilePage,name="ProfilePage"),
    path('musicians/',views.searchpage,name="searchpage"),
    path('upload/' , views.homedownload),
    path('download/<uid>/' ,views.download),
    path('handle/', views.HandleFileUpload.as_view()),
]