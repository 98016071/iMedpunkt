from django.db import models
from datetime import date

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50, default='#')
    patronymic = models.CharField(max_length=50, default='#')
    last_name = models.CharField(max_length=50, default='#')
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, default="?")
    group = models.CharField(max_length=50, default='#')
    home = models.CharField(max_length=50, default='#')
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    health = models.CharField(max_length=100, default='#')
    allergy = models.CharField(max_length=100, default='#')
    food = models.CharField(max_length=100, default='#')
    need_repeat = models.BooleanField(default=False)
    in_isolator = models.BooleanField(default=False)
    bolel = models.BooleanField(default=False)
    cert1 = models.BooleanField(default=False)
    cert2 = models.BooleanField(default=False)

    def full_name(self):
        return self.first_name + ' ' + self.patronomic + ' ' + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def age(self):
        return (date.today() - self.birth_date).days // 365

    def certificates(self):
        if self.cert1 and self.cert2:
            return '+'
        return '-'


class Visit(models.Model):
    date = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student)
    complaints = models.CharField(max_length=1000)
    examination = models.CharField(max_length=1000)
    diagnosis = models.CharField(max_length=1000)
    treatment = models.CharField(max_length=1000)
    temperature = models.FloatField(default=0)
    toPrint = models.BooleanField(default=False)
    is_first = models.BooleanField(default=False)
    injury = models.BooleanField(default=False)
    need_consultation = models.BooleanField(default=False)
    need_repeat = models.BooleanField(default=False)

    def __str__(self):
        return self.date.strftime("%d.%m.%y") + " " + self.student.__str__() + " (" + self.complaints + ")"

    def __unicode__(self):
        return self.date.strftime("%d.%m.%y") + " " + self.student.__str__() + " (" + self.complaints + ")"

