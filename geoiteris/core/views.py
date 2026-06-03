from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import College


@api_view(['GET'])
def college_list(request):
    date = []
    for c in College.objects.all():
        date.append({
            'name': c.name,
            'location': c.location,
            'latitude': c.latitude,
            'longitude': c.longitude,
        })
    return Response(data)