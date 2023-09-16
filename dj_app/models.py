from django.db import models
import time
# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.name