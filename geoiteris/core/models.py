from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    graduation_year = models.IntegerField()
    contact = models.EmailField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.graduation_year})"
    
