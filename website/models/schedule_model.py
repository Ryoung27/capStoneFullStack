from django.db import models
# from .user_model import User
# from .day_model import Day

"""
    module: Schedule Model
    author: Ronnie Young
    purpose: To create the data model for a schedule
"""


class Schedule(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    day = models.ManyToManyField('Day')
    schedule = models.CharField(max_length=1000)
# I REALLY do not want that to be a charfield, talk to Joe
# Ask if I really want to delete cascade for user?
