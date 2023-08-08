# trainee_app/models.py
from django.db import models

class Trainee(models.Model):
    trainee_id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_num = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

