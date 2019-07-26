from django.shortcuts import render
from .forms import UserForm 
from .forms import User

def register_user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserForm()
    return render(request, "register_user.html", {"form":form})


def login_user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserForm()
    return render(request, "login_user.html", {"form":form})



def update_user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserForm()
    return render(request, "update_user.html", {"form":form})






