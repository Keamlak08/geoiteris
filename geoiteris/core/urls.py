from django.urls import path
from .views import college_list

urlpatterns = [
    path('colleges/', college_list, name='college-list'),

    
]