from django.urls import path
from prova.views import *
from core.views import *

app_name = 'core_urls'
urlpatterns = [
    path('dashboard/', DashBoard_Master_User, name='dashBoard_master_user'),
    path('login/', Login_Master_User, name='login_master_user'),
    path('register/', Register_Master_User, name='register_master_user'),
    path('profile/', Profile_Master_User, name='profile_master_user'),
    path('usuarios/', Table_Master_User, name='table_master_user'),
    path('materias/', Materia_Master_User, name='materias_master_user'),
    path('provas/', display_prova_list, name='provas_master_user'),
]
