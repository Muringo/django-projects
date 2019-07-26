from django import forms
from .models import Administrator

class AdministratorForm(forms.ModelForm):
	class Meta:
		model = Administrator
		fields = "__all__"