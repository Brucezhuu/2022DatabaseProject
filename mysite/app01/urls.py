from django.urls import path

from . import views
from . import course
urlpatterns = [
    path('toLogin/', views.login, name='login'),
    path('logout/', views.logout),
    path('toRegister/', views.register, name='register'),
    path('student/login/', views.StudentLogin),
    path('student/register/', views.StudentRegister),
    path('course/', course.showCourse, name="course"),
    path('course/add/', course.course_add),
    path('course/<int:nid>/delete/', course.course_delete),
    path('course/<int:nid>/edit/', course.course_edit),
]
