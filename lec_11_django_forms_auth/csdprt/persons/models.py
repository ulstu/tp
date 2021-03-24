from django.db import models
from django.core import validators

class Person(models.Model):
	person_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50, verbose_name="Имя")
	last_name = models.CharField(max_length=50, verbose_name="Фамилия")
	patronymic = models.CharField(max_length=50, null=True, blank=True)
	bio = models.TextField(null=True, blank=True, validators=[validators.MinLengthValidator(10, message="Биография должна быть не короче 10 символов")])
	email = models.EmailField(null=True, verbose_name="email адрес")
	publications = models.TextField(null=True, blank=True)
	photo = models.ImageField(upload_to ='uploads/', null=True, blank=True)

	def __str__(self):
		return f"{self.first_name} {self.patronymic} {self.last_name}"

	class Meta:
		verbose_name_plural='Преподаватели'
		verbose_name = 'Преподаватель'
		ordering = ['-last_name']


class Course(models.Model):
	course_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, verbose_name="Наименование дисциплины", db_index=True)
	description = models.TextField(null=True, blank=True, verbose_name="Описание", validators=[validators.MinLengthValidator(10, message="Биография должна быть не короче 10 символов")])
	learning_outcomes = models.TextField(null=True, blank=True, verbose_name="Приобретаемые навыки")
	mooc_url = models.URLField(null=True, error_messages={'invalid': 'Неправильно указан URL адрес'})
	person_id = models.ForeignKey('Person', null=True, on_delete=models.PROTECT, verbose_name='Преподаватель')

	class Meta :
		verbose_name_plural = 'Дисциплины'
		verbose_name = 'Дисциплина'
		ordering= ['name']
