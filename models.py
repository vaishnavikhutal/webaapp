from django.db import models

# Create your models here.
class Book(models.Model):
    bid=models.CharField(max_length=20)
    bname = models.CharField(max_length=100)
    bauthor = models.CharField(max_length=60)
    bstatus = models.CharField(max_length=50)


class login(models.Model):
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=25)