from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    objects_list = Student.objects.all().order_by('group')
    context = {'object_list': objects_list, }
    return render(request, template, context)
