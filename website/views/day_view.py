# from rest_framework import viewsets
# from website import models


# class Day_Viewset(viewsets.ModelViewSet):
#     queryset = models.Day.objects.all()

from django.shortcuts import render
from website.models import Day

def day_view(request):
    """View for the day

    Arguments:
        GET, returns render of template with information.
    """
    #Place holder text.
    day = Day.objects.all()
    return render(request, template_name, {'data_set':data_set})
    # if request.method == "GET":
    #     day = Day.objects.all()
    #     data_set = []
    #     for day in days:
    #         #Need to work on this if function.
    #         #Based on Levi's category_view.py

    #     template_name= "website/day.html"
    #     return render(request, template_name, {'data_set':data_set})

