from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    # context = {'projects': projects}
    return render(request, 'project_index.html', {'projects': projects})



def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    # context = {'project': project}
    return render(request, 'project_detail.html', {'project': project})

# Create your views here.

# def student_detail(request, pk):
# 	student = Student.objects.get(pk=pk)
# 	return render(request, "student_detail.html", {"student":student})
