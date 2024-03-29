from django.shortcuts import render
from .models import Teacher, Student


def base(request):
    return render(request, 'base.html')
def index(request):
    return render(request, 'index.html')



def teachers(request):
    teachers_data = {'teachers': [{'nom_complet': 'John Doe'}, {'nom_complet': 'Jane Doe'}]}
    return render(request, 'teachers.html', teachers_data)

def login(request):
    # Votre logique de traitement pour la connexion
    return render(request, 'login.html')

def register(request):
    # Votre logique de traitement pour l'inscription
    return render(request, 'register.html')
def contact(request):
    # Votre logique de traitement pour la page de contact
    return render(request, 'contact.html')


def teacher_details(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'teacher_details.html', {'teacher': teacher})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})

