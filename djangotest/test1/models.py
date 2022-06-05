from os import major
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# user details table
class user_details(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250)
    class year_in_college(models.IntegerChoices):
        FIRST_YEAR = 1
        SECOND_YEAR = 2
        THIRD_YEAR = 3
        FOURTH_YEAR = 4
        FIFTH_YEAR = 5
        SIXTH_YEAR = 6
        MASTERS_DEGREE = 7
        PHD = 8
        PROFESSOR = 9
    college_year = models.SmallIntegerField(choices=year_in_college.choices)
    birthday = models.DateField()
    college_major = models.CharField(max_length=500)
    review_count = models.SmallIntegerField()

# professor details
class professor_details(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    professor_name = models.CharField(max_length=250)
    University_name = models.CharField(max_length=250)
    Department = models.CharField(max_length=250)
    Avg_Rating = models.DecimalField(max_digits=3, decimal_places=2)

