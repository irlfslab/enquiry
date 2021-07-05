from django.urls import path
from . import views


urlpatterns = [
	path('', views.list_courses, name='list_courses'),
	path('api/get_courses/', views.get_courses)
] 

