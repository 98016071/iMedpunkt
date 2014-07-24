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


def student(request, student_id):
    stud = Student.objects.get(pk=student_id)
    template = loader.get_template('student.html')
    context = RequestContext(request, {
        'stud': stud
    })
    return HttpResponse(template.render(context))

def student_post(request, student_id):
    if request.method != 'POST':
        return HttpResponse('Fuck you!')
    data = request.POST
    stud = Student.objects.get(pk=student_id)
    stud.cert1, stud.cert2, stud.health, stud.allergy = data.get('cert1', False), data.get('cert2', False), data['health'], data['allergy']
    stud.bolel, stud.height, stud.weight = data['bolel'], data['height'], data['weight']
    stud.save()
    return student_list(request)




def root(request):
    return HttpResponse("<a href='student_list'>to student list</a>")