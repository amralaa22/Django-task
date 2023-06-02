from django.db import models

# Create your models here.
class Myuser(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 12)
    email = models.EmailField(max_length = 100)