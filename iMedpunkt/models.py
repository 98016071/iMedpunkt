from django.db import models
from datetime import date

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50, default='#')
    last_name = models.CharField(max_length=50, default='#')
    patron = models.CharField(max_length=50, default='#')
    group = models.CharField(max_length=50, default='#')
    home = models.CharField(max_length=50, default='#')
    health = models.CharField(max_length=100, default='#')
    allergy = models.CharField(max_length=100, default='#')
    food = models.CharField(max_length=100, default='#')
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    cert1 = models.BooleanField(default=False)
    cert2 = models.BooleanField(default=False)
    birth_date = models.DateField()

    def full_name(self):
        return self.first_name + ' ' + self.patron + ' ' + self.last_name


    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        return (date.today() - self.birth_date).days // 365
    def certificates(self):
        return '+'