from django.db import models


class Regi(models.Model):
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=100)


class UserData(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateTimeField()


class Destination(models.Model):
    image = models.ImageField(upload_to='travel/')
    place = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
