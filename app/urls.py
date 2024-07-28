from django.urls import  path
from .views import *
from .views import register_user, user_login, user_logout
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter 

router = DefaultRouter()
router.register('Lesson', LessonViewSet, basename='lesson')
router.register('Student', StudentViewSet, basename='Student')
router.register('Assignment', AssignmentViewSet, basename='Assignment')

router.register('Teacher', TeacherViewSet, basename='Teacher')
router.register('Attendance', AttendanceViewSet, basename='Attendance')
router.register('Grade', GradeViewSet, basename='Grade')

urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),
  path('register/', register_user, name='register'),
  path('login/', user_login, name='login'),
  path('logout/', user_logout, name='logout'),
  path('change_password/', change_password, name='change_password'),




]







