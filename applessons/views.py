from django.shortcuts import render

# Create your views here.
from applessons.models import Applessons
from students.models import Students


def getLessons(request):
    listLessons = Applessons.objects.all()
    contexto = {'list': listLessons}
    return render(request, 'lessons/list_lessons.html', contexto)

def listStudentsClass(request, id_class):
    listStudents = Students.objects.filter(lessons_id = id_class)
    nameMatter = Applessons.objects.filter(id = id_class)
    print(nameMatter)
    contexto = {'list': listStudents, 'nameMatter': nameMatter}
    return render(request, 'lessons/list_students_class.html', contexto)

