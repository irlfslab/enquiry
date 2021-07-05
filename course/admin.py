from django.contrib import admin

# Register your models here.
from .models import Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name','start_date','end_date','location']
