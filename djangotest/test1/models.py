from dataclasses import field
from email.policy import default
from os import major
from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse

# default values
DEFAULT_VAL = "no_user"

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
    university_name = models.CharField(max_length=250, blank=True)
    birthday = models.DateField(blank=True)
    college_major = models.CharField(max_length=250, blank=True)
    review_count = models.SmallIntegerField(blank=True)
    Avg_Rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, default= 1.0)
    Department = models.CharField(max_length=250, blank=True)
    recent_posts = models.JSONField(blank=True)
    recent_comments = models.JSONField(blank=True)

class posts(models.Model):
    post_title = models.CharField(max_length=250)
    post_content = models.TextField()
    post_id = models.AutoField(primary_key=True)
    post_time = models.DateTimeField()
    user_id = models.ForeignKey(User, default=DEFAULT_VAL, on_delete=models.SET_DEFAULT)
    posts_comments = models.JSONField(blank=True)
    posts_likes = models.IntegerField(default=0)
    posts_dislikes = models.IntegerField(default=0)
    posts_report = models.CharField(max_length=250, blank = True)
    posts_report_description = models.TextField(blank=True)

class review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, default=DEFAULT_VAL, on_delete=models.SET_DEFAULT)
    review_title = models.CharField(max_length=250)
    review_details = models.TextField()
    review_comments = models.JSONField(blank=True)
    course_name = models.TextField()
    review_time = models.DateTimeField()
    review_rating = models.IntegerField()
    review_likes = models.IntegerField(default=0)
    review_dislikes = models.IntegerField(default=0)
    review_report = models.CharField(max_length=250, blank = True)
    review_report_description = models.TextField(blank=True)