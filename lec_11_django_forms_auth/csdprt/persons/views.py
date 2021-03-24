from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person, Course
from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import CourseForm
from django.contrib.auth.models import Permission


def get_user_permissions(user):
    if user.is_superuser:
        return Permission.objects.all()
    return user.user_permissions.all() | Permission.objects.filter(group__user=user)

class CourseCreateView(CreateView):
	template_name = 'persons/create_course.html'
	form_class = CourseForm
	#success_url = "persons:all_persons"

	def get_context_data (self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dummy'] = 5
		return context

	def get_success_url(self):
		return reverse_lazy("persons:teacher_course", kwargs={"person_id": self.object.person_id.person_id})

class CourseUpdateView(UpdateView):
	template_name = 'persons/create_course.html'
	model = Course
	form_class = CourseForm

	def get_context_data (self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dummy'] = 5
		return context

	def get_success_url(self):
		return reverse_lazy("persons:teacher_course", kwargs={"person_id": self.object.person_id.person_id})

class CourseListView(ListView):
	model = Course
	queryset = Course.objects.order_by('-name')
	template_name = "persons/all_courses.html"

	def get_context_data(self, **kwargs):
		context = super(CourseListView, self).get_context_data(**kwargs)
		context['some_data'] = 'This is just some data!!!'
		return context

class CourseDeleteView(DeleteView):
	model = Course
	template_name = 'persons/course_delete.html'

	def get_success_url(self):
		return reverse_lazy("persons:teacher_course", kwargs={"person_id": self.object.person_id.person_id})

def index(request) :
	return render(request, "persons/index.html")

def view_persons(request):
	persons = Person.objects.order_by('-last_name')
	return render(request, "persons/persons.html", {'persons': persons})

def view_teacher_courses(request, person_id):
	courses = Course.objects.filter(person_id=person_id)
	teacher = Person.objects.get(pk=person_id)
	return render(request, "persons/teacher_courses.html", {'teacher': teacher, 'courses': courses}, content_type='text/html; charset=utf-8')

def remove_course(request, course_id):
	Course.objects.filter(pk=course_id).delete()
	return redirect('persons:index')