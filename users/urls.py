from . import views
from django.urls import path

urlpatterns = [
    path('', views.StudentListView.as_view, name = 'student_chagelist'),
    path('add/', views.StudentCreateView.as_view, name = 'student_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view, name = 'student_change'),
]