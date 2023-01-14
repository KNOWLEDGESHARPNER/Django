from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField(default='None')
    email=models.TextField(default='None')
    password=models.TextField(default='None')
    subject=models.TextField(default='None')
    mob=models.BigIntegerField(default=0)
