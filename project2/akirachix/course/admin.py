from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ("name", "duration_in_months", "description", "course_number")
	search_fields = ("name", "course_number")
	list_filter = ("course_number", "description" )
admin.site.register(Course,CourseAdmin)


# Register your models here.
 