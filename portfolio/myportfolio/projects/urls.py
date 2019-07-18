from django.urls import path
from . import views
from .views import project_index, project_detail


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
