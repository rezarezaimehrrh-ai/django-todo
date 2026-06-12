from django.urls import path
from . import views


urlpatterns=[


path('', views.add_task , name='add_page') ,
path('done/', views.check_task, name='boolpage'),
path('delete/', views.delete_task, name='delpage'),
path('edit/', views.edit_task, name='edpage'),
path('un_done/',views.undone_task, name='un_donepage'),




 ]
