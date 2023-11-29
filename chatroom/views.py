from django.shortcuts import render, redirect
from chatroom import forms as room_form
from chatroom import models as chatroom_model
# Create your views here.

def MyRooms(request):

    rooms = chatroom_model.Room.objects.filter(rcreated_by=request.user)
    context={
        "rooms":rooms
    }
    return render(request, "chatroom/rooms.html", context)

def AllRooms(request):
    rooms = chatroom_model.Room.objects.all()
    context={
        "rooms":rooms
    }
    return render(request, "chatroom/rooms.html", context)

def CreateRoom(request):
    form = room_form.CreateroomForm()

    if request.method == "POST":
        form = room_form.CreateroomForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.user.id)
            form.instance.rcreated_by=request.user
            form.save()
            return redirect('home')

    context = {
        'form':form
    }

    return render(request, 'chatroom/createroom.html', context)

def chat(request):
    return render(request, 'chatroom/chat.html')