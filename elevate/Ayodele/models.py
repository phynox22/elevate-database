from django.db import models

# Create your models here.
class Movie(models.Model):
    MY_CHOICES = (
        
        ('a', 'Sci-fi'),
        ('b', 'Romance'),
        ('c', 'Action'),
        ('d', 'Horror'),
        ('e', 'Thriller'),
        ('f', 'Comedy'),
        
    )
    
    title = models.CharField(max_length=355)
    
    category = models.CharField(max_length=1, choices=MY_CHOICES)


