from student.models import Student
from teachers.models import Teachers
from course.models import Course
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"

class TeachersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teachers
		fields = "__all__"
	
class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = "__all__"
	
		
	
		