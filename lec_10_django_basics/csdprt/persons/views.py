from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader
from django.shortcuts import render

def index(request) :
	s = 'Список сотрудников \n'
	for p in Person.objects.order_by('-last_name'):
		s += str(p) + "\n"
	return HttpResponse(s, content_type='text/plain; charset=utf-8')

def allpersons(request):
	template = loader.get_template('persons/persons.html')
	persons = Person.objects.order_by('-last_name')
	context = {'persons': persons}
	return HttpResponse(template.render(context, request), content_type='text/html; charset=utf-8')

def allpersonssh(request):
	persons = Person.objects.order_by('-last_name')
	return render(request, "persons/persons.html", {'persons': persons}, content_type='text/html; charset=utf-8')