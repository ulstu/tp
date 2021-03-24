from django.urls import path
from .views import *

app_name='persons'

urlpatterns = [
	path ('', index, name='index'),
	path ('all/', view_persons, name='all_persons'),
	path('<int:person_id>/', view_teacher_courses, name="teacher_course"),
	path('course/<slug:pk>/remove/', CourseDeleteView.as_view(), name="remove_course"),
	path('course/<slug:pk>/edit/', CourseUpdateView.as_view(), name="update_course"),
	path('course/all', CourseListView.as_view(), name='all_courses'),
	path('addcourse/', CourseCreateView.as_view(), name='add_course'),
]