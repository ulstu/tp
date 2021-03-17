from django.urls import path
from .views import *

urlpatterns = [
	path ('', persons, name='index'),
	path('<int:person_id>/', teachercourses, name="teacher_course"),
]