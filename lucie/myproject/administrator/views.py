from django.shortcuts import render
from .forms import AdministratorForm
from .models import Administrator
	
def list_administrator(request):
	administrators=Administrator.objects.all()
	return render(request, "list_administrator.html",{"administrators":administrators})

# Create your views here.
