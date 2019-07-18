from django.shortcuts import render
from student.models import Student
from .serializer import StudentSerializer
from teachers.models import Teachers
from .serializer import TeachersSerializer
from course.models import Course
from .serializer import CourseSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class TeachersViewSet(viewsets.ModelViewSet):
	queryset = Teachers.objects.all()
	serializer_class = TeachersSerializer


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer



# Create your views here.
