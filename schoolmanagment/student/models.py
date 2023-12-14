from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth = models.DateField()
    class_st=models.IntegerField()
    gender=models.CharField(max_length=50)
    place = models.CharField(max_length=40)