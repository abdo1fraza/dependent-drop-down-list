from django.shortcuts import render
from users.models import Student, Branch
from users.forms import StudenForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

class StudentListView(ListView):
    model = Student
    form_class = StudenForm
    context_object_name = 'Student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudenForm
    success_url = reverse_lazy('student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudenForm
    success_url = reverse_lazy('student_changelist')    


