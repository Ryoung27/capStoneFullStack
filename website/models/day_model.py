from django.db import models
# from .schedule_model import Schedule
# from .user_model import User

"""
    module: Day Model
    author: Ronnie Young
    purpose: To create the data model for a day.
"""


class Day(models.Model):
    # schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    distance = models.CharField(max_length=10)
    thoughts = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
