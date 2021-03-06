from django.conf.urls import url, include
from .views import StudentViewSet
from .views import TeachersViewSet
from .views import CourseViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("students", StudentViewSet)
router.register("teachers", TeachersViewSet)
router.register("course", CourseViewSet)


urlpatterns = [
url("", include(router.urls)),
]   