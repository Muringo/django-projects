from django.db import models

class Register(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	date_of_birth = models.DateField()
	password = models.IntegerField(max_length=15)
	confirm_password = models.IntegerField(max_length=15)
	id_number = models.IntegerField(max_length=10)

# Create your models here.
