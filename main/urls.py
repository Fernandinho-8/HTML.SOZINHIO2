from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list,name='task_list'),
    path('concluida', views.task_ok,name='task_ok'),
    path('pendente', views.task_nok, name='task_nok' ),
    path('create_task', views.task_create, name='task_create'),
]
