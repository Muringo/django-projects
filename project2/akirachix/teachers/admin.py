from django.contrib import admin
from .models import Teachers


class TeachersAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "registration_number", "gmail", "id_number", "image")
	search_fields = ("registration_number", "gmail", "last_name")
	list_filter = ("first_name", "date_of_birth")
admin.site.register(Teachers,TeachersAdmin)

# Register your models here.
