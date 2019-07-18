from django.db import models
from teachers.models import Teachers
teachers = models.ForeignKey(Teachers,on_delete=models.PROTECT)



# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=50)
	duration_in_months = models.IntegerField()
	course_number = models.CharField(max_length=50)
	description = models.TextField()


