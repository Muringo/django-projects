from django.db import models
from user.models import User

class Administrator(models.Model):
	product_name=models.CharField(max_length=60)
	product_image=models.ImageField(upload_to='profile_image',blank=True)
	product_description=models.TextField(blank=True)
	user=models.ForeignKey(User, on_delete=models.PROTECT)
	

def __str__(self):
	return self.product_name

# Create your models here.
