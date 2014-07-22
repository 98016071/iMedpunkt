from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from iMedpunkt.models import Student


def student_list(request):
    students = list(Student.objects.order_by("first_name"))
    template = loader.get_template('students_list.html')
    students.sort(key=lambda x: x.last_name)
    context = RequestContext(request, {
        'students': students
    })
    return HttpResponse(template.render(context))

def root(request):
    return HttpResponse("<a href='hello'>to Hello</a>")