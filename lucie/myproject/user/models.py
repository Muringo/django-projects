from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10, default=" ")
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

    