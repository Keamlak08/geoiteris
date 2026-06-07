from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Min, Max
from .models import College, Student


def college_list(request):
    data = []
    for c in College.objects.all():
        data.append({
            'name': c.name,
            'location': c.location,
            'latitude': c.latitude,
            'longitude': c.longitude,
            'student_count': c.student_count,
        })
    return JsonResponse(data, safe=False)


def home(request):
    years = Student.objects.aggregate(
        min_year=Min('graduation_year'),
        max_year=Max('graduation_year')
    )
    min_y, max_y = years['min_year'], years['max_year']

    if min_y and max_y:
        year_range = str(min_y) + '-' + str(max_y)
    else:
        year_range = None

    context={
        'student_count': Student.objects.count(),
        'college_count': College.objects.count(),
        'github_count': Student.objects.exclude(github='').exclude(github=None).count(),
        'year_range': year_range,
        'students' : Student.objects.select_related('college').order_by('-graduation_year', 'name'),
    }

    return render(request, 'core/home.html', context)

