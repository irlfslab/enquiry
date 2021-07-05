from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=30)