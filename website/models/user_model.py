from django.db import models
# from .schedule_model import ScheduleId

"""
    module: user_model
    author: Ronnie Young
    purpose: To create the data model for a user
"""


class User(models.Model):
    # schedule_id = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    user = models.CharField(max_length=88)
    email = models.CharField(max_length=96)
# I really need to speak to them about passwords on Tuesday