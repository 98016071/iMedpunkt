from datetime import date, timedelta
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from django.db import models
from django.utils import timezone
from datetime import datetime
from iMedpunkt.models import Student, Visit


def login(request):
    return HttpResponse()


def student_list(request):
    # if not request.user.is_authenticated():
    # return HttpResponseRedirect('/login/?next=%s' % request.path)
    students = list(Student.objects.order_by("first_name"))
    template = loader.get_template('students_list.html')
    students.sort(key=lambda x: x.last_name)
    context = RequestContext(request, {
        'students': students
    })
    return HttpResponse(template.render(context))


def student(request, student_id):
    student = Student.objects.get(pk=student_id)
    visits = Visit.objects.filter(student__id=student_id).order_by("date").reverse()
    template = loader.get_template('student.html')
    context = RequestContext(request, {
        'student': student,
        'visits': visits
    })
    return HttpResponse(template.render(context))


def student_post(request, student_id):
    if request.method != 'POST':
        return HttpResponse('Use POST')
    data = request.POST
    stud = Student.objects.get(pk=student_id)
    stud.cert1, stud.cert2, stud.health, stud.allergy, stud.food = \
        data.get('cert1', False), data.get('cert2', False), \
        data['health'], data['allergy'], data['food']
    stud.bolel, stud.height, stud.weight = \
        bool(int(data['bolel'])), data['height'], data['weight']
    print(data, bool(int(data['bolel'])))
    stud.save()
    return student_list(request)


def visits_list(request):
    visits = Visit.objects.order_by("date").reverse()
    today = []
    yesterday = []
    this_week = []
    earlier = []
    for visit in visits:
        visit_date = date(visit.date.year, visit.date.month, visit.date.day)
        print(visit_date)
        if visit_date == date.today():
            today.append(visit)
        elif visit.date == date.today() - timedelta(days=1):
            yesterday.append(visit)
        else:
            earlier.append(visit)

    template = loader.get_template('visits_list.html')
    context = RequestContext(request, {
        'today': today,
        'yesterday': yesterday,
        'earlier': earlier
    })
    return HttpResponse(template.render(context))


def visit_edit(request, visit_id):
    visit = Visit.objects.get(pk=visit_id)
    template = loader.get_template('visit_edit.html')
    context = RequestContext(request, {
        'visit': visit
    })
    return HttpResponse(template.render(context))


def visit_new(request, student_id):
    print('visit_new')
    visit = Visit()
    visit.student = Student.objects.get(pk=student_id)
    visit.save()
    return visit_edit(request, visit.id)


def visit_post(request, visit_id):
    if request.method != 'POST':
        return HttpResponse('Use POST')
    visit = Visit.objects.get(pk=visit_id)
    data = request.POST
    visit.complaints = data['complaints']
    visit.examination = data['examination']
    visit.diagnosis = data['diagnosis']
    visit.treatment = data['treatment']
    visit.to_print = bool(int(data['print']))  # bool(int('0')) == False
    visit.student.in_isolator = bool(int(data['isolator']))
    visit.is_first = bool(int(data['is_first']))
    visit.injury = bool(int(data['injury']))
    visit.need_consultation = bool(int(data['need_consultation']))
    visit.student.need_repeat = bool(int(data['need_repeat']))
    a, b = [int(i) for i in data['datepicker'].split('/')], [int(i) for i in data['timepicker'].split(':')]
    print(type(visit.date))
    visit.date = datetime(a[2], a[0], a[1], b[0], b[1], b[2])
    date1 = timezone.localtime(visit.date)
    visit.date = date1
    print(data, visit)
    visit.student.save()
    visit.save()
    return student(request, visit.student.id)


def root(request):
    return HttpResponse("<a href='student_list'>to student list</a>")
