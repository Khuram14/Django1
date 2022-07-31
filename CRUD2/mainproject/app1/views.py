from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from .forms import RoomForm


rooms = [
    {'id':1, 'name':'Lets learn Python!'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Front end Developer'},
]
def home(request):
    context = {'rooms':rooms}
    return render(request,'home.html', context )

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}

    return render(request,'room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'room_form.html', context)
