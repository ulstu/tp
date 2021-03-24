from django.forms import ModelForm
from .models import Person, Course


class CourseForm(ModelForm) :
    class Meta:
        model = Course
        fields = ('course_id', 'name', 'description', 'learning_outcomes', 'person_id')