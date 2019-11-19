from django.conf.urls import url
from .views import add_teacher, list_teacher, teacher_detail, edit_teacher

urlpatterns = [
    url("add/", add_teacher, name="add_teacher"),
    url("list/", list_teacher, name="list_teacher"),
    url("detail/<int:pk>/", teacher_detail, name="teacher_detail"),
    url("edit/<int:pk>/", edit_teacher, name="edit_teacher"),
]

