from django.urls import path
from .views import *

urlpatterns = [
	path ('', index),
	path('allpersons', allpersons),
	path('allpersonssh', allpersonssh),
]