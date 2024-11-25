from django.db import models
# Create your models here.
class database(models.Model):
    email=models.TextField(max_length=40)
    password=models.TextField(max_length=70)