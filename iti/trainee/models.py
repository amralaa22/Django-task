from django.db import models
from course.models import *
# Create your models here.

class Trainees(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.TextField()
    courseid = models.ForeignKey('course.Courses',on_delete = models.CASCADE)
