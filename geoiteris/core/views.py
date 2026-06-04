from django.shortcuts import render
from django.http import JsonResponse
from .models import College


def college_list(request):
    data = []
    for c in College.objects.all():
        data.append({
            'name': c.name,
            'location': c.location,
            'latitude': c.latitude,
            'longitude': c.longitude,
        })
    return JsonResponse(data, safe=False)


def home(request):
    return render(request, 'core/home.html')

