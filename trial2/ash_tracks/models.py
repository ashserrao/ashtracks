from django.db import models

# Create your models here.

class Artists(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email_id = models.EmailField(max_length=30)

    def __str__(self):
        return self.First_name

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email

class Register(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=200)
    discription = models.TextField()

    def __str__(self):
        return self.email
