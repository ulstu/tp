# Основы Django

![mvc pattern](img/mvc.png)

* Установка
```bash
django-admin startproject csdprt
```

* Запуск отладочного веб-сервера

```bash
manage.py runserver
```

* Создание приложения
```bash
manage.py startapp persons
```

* Регистрирация приложения в INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'persons.apps.PersonsConfig',
]

```

* Добавление контроллера во views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
	return HttpResponse("Здecь будет выведен список преподавателей")
```

* определение urls.py приложения
```python
from django.urls import path
from .views import index 

urlpatterns = [
	path ('', index),
]
```

* определение urls.py проекта
```python
path ('persons/', include('persons.urls')),
```

* добавление модели

```python
class Person(models.Model):
	person_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	patronymic = models.CharField(max_length=50, null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	publications = models.TextField(null=True, blank=True)
	photo = models.ImageField(upload_to ='uploads/', null=True, blank=True)
```

* создание миграции

```bash
python manage.py makemigrations persons
python manage.py sqlmigrate persons 0001
python manage.py migrate
```

* manage shell
```bash
python manage.py shell

```

```python
from persons.models import Person

p = Person(first_name="Иван", last_name="Иванов", patronymic="Иванович", bio="родился, учился и работает", publications="много")
p.save()

Person.objects.create(first_name="Петр", last_name="Петров", patronymic="Петрович", bio="родился, учился и не работает", publications="мало")

for i in Person.objects.all(): print(i.first_name)

Person.objects.get(pk=2).first_name
d = Person.objects.get(pk=2)
d.delete()
```

* редактирование модели в контроллере
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index(request) :
	s = 'Список сотрудников \n'
	for p in Person.objects.order_by('-last_name'):
		s += str(p) + "\n"
	return HttpResponse(s, content_type='text/plain; charset=utf-8')
```

## Шаблоны
Шаблон Django - это файл с НТМL-кодом страницы, содержащий особые команды шаблонизатора: директивы, теги и фильтры. Директивы указывают поместить в заданное место НТМL-кода какое-либо значение, теги управляют генерировани­ем содержимого, а фильтры выполняют какие-либо преобразования указанного значения перед выводом.

По умолчанию шаблонизатор ищет все шаблоны в папках templates, вложенных в папки пакетов приложений. Сами файлы шаблонов веб­ страниц должны иметь расширение html.

persons/templates/persons/index.html

```html
<!DOCTYPE html>
<html>
	<head>
	<meta charset="UTF-8">
	<titlе>Главная : : Страница сотрудников</titlе>
	</head>
	<body>
		<h1>Сорудники</h1>
		{% for p in persons %}
		<div>
		<h2>{{ p.first_name }} {{ p.last_name }} {{ p.patronymic }}</h2>
		<р>{{ p.bio }}</р>
		<р>{{ p.publications}}</р>
		</div>
		{% endfor %}
	</body>
</html>
```

* использование шаблонов
```python
def allpersons(request):
	template = loader.get_template('persons/persons.html')
	persons = Person.objects.order_by('-last_name')
	context = {'persons': persons}
	return HttpResponse(template.render(context, request), content_type='text/html; charset=utf-8')

def allpersonssh(request):
	persons = Person.objects.order_by('-last_name')
	return render(request, 'persons/persons.html ', {'persons': persons})
```


##  Административный веб-сайт
```bash 
python manage.py createsuperuser
```

* в admin.py
```python
from persons.models import Person
admin.site.register(Person)
```

```python
class PersonAdmin(admin.ModelAdmin) :
    list_display = ('person_id', 'first_name', 'patronymic', 'last_name')
    list_display_links = ('first_name' , 'last_name')
    search_fields = ( 'first_name' , 'last_name')

admin.site.register(Person, PersonAdmin)

```

models.py
```python
class Person(models.Model):
	person_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=50, verbose_name="Имя")
	last_name = models.CharField(max_length=50, verbose_name="Фамилия")
	patronymic = models.CharField(max_length=50, null=True, blank=True)
	bio = models.TextField(null=True, blank=True)
	publications = models.TextField(null=True, blank=True)
	photo = models.ImageField(upload_to ='uploads/', null=True, blank=True)

	def __str__(self):
		return f"ФИО: {self.first_name} {self.patronymic} {self.last_name}"

	class Meta:
		verbose_name_plural='Персоналии'
		verbose_name = 'Сотрудники'
		ordering = ['-last_name']
```

views.py
```python
def allpersons(request):
	template = loader.get_template('persons/persons.html')
	persons = Person.objects.order_by('-last_name')
	context = {'persons': persons}
	return HttpResponse(template.render(context, request), content_type='text/html; charset=utf-8')

def allpersonssh(request):
	persons = Person.objects.order_by('-last_name')
	return render(request, 'persons/persons.html ', {'persons': persons})
```

# Запись лекции
https://youtu.be/8pvODiWW1dM
