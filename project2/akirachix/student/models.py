from django.db import models
from course.models import Course
course=models.ManyToManyField(Course)

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    registration_number = models.CharField(max_length=20)
    place_of_residence = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    gmail = models.EmailField()
    guardian_name = models.CharField(max_length=20)
    id_name = models.IntegerField()
    date_joined = models.DateField(max_length=20)
    image = models.ImageField(upload_to='profile_pics', blank = True)


    def __str__(self):
        return self.first_name + " " +self.last_name