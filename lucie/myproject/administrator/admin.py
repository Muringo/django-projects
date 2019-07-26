from django.contrib import admin
from .models import Administrator

class AdministratorAdmin(admin.ModelAdmin):
	list_display=("product_image","product_name", "product_description")
	search_fields=("product_name",)

admin.site.register(Administrator)

# Register your models here.
