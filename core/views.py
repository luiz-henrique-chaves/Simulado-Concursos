from django.shortcuts import render
from disciplina.models import DisciplinaModel
from prova.models import ProvaModel


def TemplateIndex(request):
    return render(
        request,
        'enduser/index.html'
    )

def DashBoard_Master_User(request):
    return render(
        request,
        'masteruser/index.html'
    )

def Profile_Master_User(request):
    return render(
        request,
        'masteruser/profile.html'
    )

def Table_Master_User(request):
    return render(
        request,
        'masteruser/table.html'
    )

def Materia_Master_User(request):
    return render(
        request,
        'masteruser/materias.html',
        {
            'materias' : DisciplinaModel.objects.all(),
        }

    )
    
def Login_Master_User(request):
    return render(
        request,
        'masteruser/login.html'
    )

def Register_Master_User(request):
    return render(
        request,
        'masteruser/register.html'
    )
