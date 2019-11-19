from django.db import models
from teachers.models import Teachers




# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=50)
	duration_in_months = models.IntegerField()
	course_number = models.CharField(max_length=50)
	description = models.TextField()
	teachers = models.ForeignKey(Teachers, on_delete=models.PROTECT, related_name="courses", null= True)


	def full_name(self):
		return "{} {}".format(
			self.first_name,
            self.last_name
            )


