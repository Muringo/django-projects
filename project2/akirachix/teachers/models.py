from django.db import models

# Create your models here.
class Teachers(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	registration_number = models.CharField(max_length=20)
	place_of_residence = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	gmail = models.EmailField()
	id_number = models.IntegerField()
	image = models.ImageField(upload_to='profile_pics', blank = True)

	def full_name(self):
		return "{} {}".format(
			self.first_name,
			self.last_name
			)