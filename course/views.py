from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def list_courses(request):
	all_courses = Course.objects.all()
	return render(request, 'course.html', {'all_courses': all_courses})


@api_view(['GET'])
def get_courses(request):
	location = request.query_params.get('location', None)
	sort_courses = request.query_params.get('sort_courses', None)
	sort_start_date = request.query_params.get('sort_start_date', None)
	#
	print("location:",location)
	print("sort_courses:", sort_courses)
	print("sort_start_date:", sort_start_date)
	
	courses = Course.objects.all()
	print("courses:",courses)
	if location:
		courses = courses.filter(location=location)
	if sort_courses:
		if sort_courses == 'ascending':
			courses = courses.all().order_by('course_name')
		elif sort_courses == 'descending':
			courses = courses.all().order_by('-course_name')
	if sort_start_date:
		if sort_start_date == 'ascending':
			courses = courses.all().order_by('start_date')
		elif sort_start_date == 'descending':
			courses = courses.all().order_by('-start_date')

	if courses:
		serialized = CourseSerializer(courses, many=True)
		print("after serialize:", serialized)
		print("serialized data", serialized.data)
		return Response(serialized.data)
	else:
		print("exec else from courses:")
		return Response({})


