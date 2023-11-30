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
            form.instance.rcreated_by=request.user
            form.save()
            form.instance.ruser.add(request.user)
            return redirect('myroom')

    context = {
        'form':form
    }

    return render(request, 'chatroom/createroom.html', context)

def joinroom(request, rslug):
    try:
        room = chatroom_model.Room.objects.get(rslug=rslug)
        room.ruser.add(request.user)
        return redirect('chat', room.rslug)
    except Exception as e:
        messaage.error(request, "Room not find")
        return redirect('room')

def joinedroom(request):

    rooms = chatroom_model.Room.objects.filter(ruser=request.user)

    context = {
        'rooms':rooms
    }
    return render(request, 'chatroom/rooms.html', context)

def chat(request, rslug):
    room = chatroom_model.Room.objects.get(rslug=rslug)
    context={
        'room':room
    }
    return render(request, 'chatroom/chat.html', context)