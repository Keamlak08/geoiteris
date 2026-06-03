from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    graduation_year = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.graduation_year} - {self.college.name}"
    
