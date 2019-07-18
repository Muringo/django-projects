from django.shortcuts import render
from .forms import TeacherForm
from .models import Teachers

def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherForm()
    return render(request, "add_teacher.html", {"form":form})



def list_teacher(request):
    teacher = Teachers.objects.all()
    return render(request, "list_teacher.html", {"teacher":teacher})



def teacher_detail(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    return render(request, "teacher_detail.html", {"teacher":teacher})



def edit_teacher(request, pk):
    if request.method == "POST":
        form = TeacherForm(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
            return redirect("list_teacher")
    else:
        form = TeacherForm(instance = teachers)
    return render(request, "edit_teacher.html", {"form":form})
            

# Create your views here.