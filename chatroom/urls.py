from django.urls import path
from chatroom import views as chatroom_view

urlpatterns = [
    path('createroom/', chatroom_view.CreateRoom, name="createroom"),
    path('myroom/', chatroom_view.MyRooms, name="myroom"),
    path('allroom/', chatroom_view.AllRooms, name="allroom"),
    path('chat/', chatroom_view.chat, name="chat"),
]