from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, Course
from django.template import loader
from django.shortcuts import render

def index(request) :
	s = 'Список сотрудников \n'
	for p in Person.objects.order_by('-last_name'):
		s += str(p) + "\n"
	return HttpResponse(s, content_type='text/plain; charset=utf-8')

def persons(request):
	persons = Person.objects.order_by('-last_name')
	return render(request, "persons/index.html", {'persons': persons})

def teachercourses(request, person_id):
	courses = Course.objects.filter(person_id=person_id)
	teacher = Person.objects.get(pk=person_id)
	return render(request, "persons/teacher_courses.html", {'teacher': teacher, 'courses': courses}, content_type='text/html; charset=utf-8')
