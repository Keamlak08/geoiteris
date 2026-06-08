from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Count, Min, Max
from .models import College, Student
from django.contrib.admin.views.decorators import staff_member_required


def college_list(request):
    colleges = College.objects.annotate(student_count=Count('student'))
    data = []
    for c in colleges:
        data.append({
            'name': c.name,
            'location': c.location,
            'latitude': c.latitude,
            'longitude': c.longitude,
            'student_count': c.student_count,
            'logo_url' : c.logo_url or '',
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

@staff_member_required
def manage(request):
    context = {
        'colleges': College.objects.order_by('name'),
    }
    return render(request, 'core/manage.html', context)

@staff_member_required
def add_college(request):
    if request.method == 'POST':
        College.objects.create(
            name=request.POST.get('name'),
            location=request.POST.get('location'),
            latitude=float(request.POST.get('latitude', 0)),
            longitude=float(request.POST.get('longitude', 0)),
            logo_url=request.POST.get('logo_url') or None,
        )
    return redirect('manage')

@staff_member_required
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            graduation_year=int(request.POST.get('graduation_year')),
            college_id=int(request.POST.get('college')),
            github=request.POST.get('github') or None,
            contact=request.POST.get('contact') or None,
        )
    return redirect('manage')