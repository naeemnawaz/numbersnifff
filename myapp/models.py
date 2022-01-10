from django.db import models

# Create your models here.
class Contact(models.Model):

    username = models.CharField(max_length=50)
    email = models.EmailField(null= True)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=50) #(blank = True)



class Subscribers(models.Model):
    Sub_email = models.EmailField(null= True)
    data = models.DateTimeField(auto_now_add=True)



