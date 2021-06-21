from django.shortcuts import render

# Create your views here.
from applessons.models import Applessons
from students.models import Students


def getStudents(request):

    listStudents = Students.objects.all()
    print(listStudents)
    contexto = {'listStudents': listStudents}

    return render(request, 'students/students_list.html', contexto)

def getIdStudent(request, id_students):
    studentsId = Students.objects.filter(id = id_students)
    contexto = {'sudentsId': studentsId}
    return render(request, 'students/students_detalle.html', contexto)

def home(request):
    contexto = {}
    return render(request, 'students/home.html', contexto)
