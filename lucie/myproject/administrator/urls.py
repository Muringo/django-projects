from django.urls import path
from .views import list_administrator


urlpatterns=[
path("administrator/", list_administrator, name="list_administrator"),
]