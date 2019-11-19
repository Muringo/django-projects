from django.db import models
from course.models import Course
import datetime
from django.core.exceptions import ValidationError

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
    courses=models.ManyToManyField(Course, related_name="students")


    def __str__(self):
        return self.first_name + " " +self.last_name


    def full_name(self):
        return "{} {}".format(
                self.first_name,
                self.last_name
                )

        def get_age(self):
            today = datetime.date.today()
            return today.year - self.date_of_birth.year
            age = property(get_age)

            def clean(self):
                age = self.age
                if age <18 or age>30:
                    raise ValidationError("Only above 17 years and Above 30 years")
                    return age

    def teachers(self):
        return [course.teachers for course in self.courses.all()]
   
          