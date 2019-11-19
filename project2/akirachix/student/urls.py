from django.conf.urls import url
from .views import add_student, list_students, student_detail, edit_student

urlpatterns = [
    url("add/", add_student, name="add_student"),
    url("list/", list_students, name="list_students"),
    url("detail/<int:pk>/", student_detail, name="student_detail"),
    url("edit/<int:pk>/", edit_student, name="edit_student"),
]