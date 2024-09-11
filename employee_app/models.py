from django.db import models

# Create your models here.
class Employee_details(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25)
    address=models.TextField()
    is_active=models.BooleanField(default=True)
