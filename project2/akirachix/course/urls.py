from django.conf.urls import url
from .views import add_course, list_course, course_detail, edit_course

urlpatterns = [
    url("add/", add_course, name="add_course"),
    url("list/", list_course, name="list_course"),
    url("detail/<int:pk>/", course_detail, name="course_detail"),
    url("edit/<int:pk>/", edit_course, name="edit_course"),
]