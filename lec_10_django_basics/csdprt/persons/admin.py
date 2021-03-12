from django.contrib import admin
from persons.models import *

class PersonAdmin(admin.ModelAdmin) :
    list_display = ('person_id', 'first_name', 'patronymic', 'last_name')
    list_display_links = ('first_name' , 'last_name')
    search_fields = ( 'first_name' , 'last_name')

class CourseAdmin(admin.ModelAdmin) :
    list_display = ('course_id', 'name', 'person_id')
    list_display_links = ('name' , 'person_id')
    search_fields = ('name', 'person_id')

admin.site.register(Person, PersonAdmin)
admin.site.register(Course, CourseAdmin)
