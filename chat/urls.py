from django.urls import path
from . import views
urlpatterns = [
    path('chat/', views.messages_page,name="messages_page"),
]
