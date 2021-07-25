from django.db import models

# Create your models here.

class Basicdetails(models.Model):
   first_name = models.CharField(max_length=12)
   last_name = models.CharField(max_length=12)
   father_name = models.CharField(max_length=12)
   mother_name = models.CharField(max_length=12)
   date_of_birth = models.DateField()
   gender = models.CharField(max_length=6)
   about = models.TextField()


   def __str__(self):
      return self.first_name

class Education(models.Model):
   course_name = models.CharField(max_length=20)
   university_name = models.CharField(max_length=40)
   passing_year = models.IntegerField()

   def __str__(self):
      return self.course_name

