from django.contrib import admin
from django.urls import path, include
from core.views import home, manage, add_college, add_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', home, name='home'),
    path('manage/', manage, name='manage'),
    path('manage/add-college/', add_college, name='add-college'),
    path('manage/add-student/', add_student, name='add-student'),
]

