from django.db import models

# Create your models here.

class Position (models.Model):
     title = models.CharField(max_length = 20)

class Employee (models.Model):
     fullname = models.CharField(max_length = 60)
     emp_code = models.CharField(max_length = 60)
     mobile = models.CharField(max_length = 60)
     position = models.ForeignKey(Position, on_delete = models.CASCADE)