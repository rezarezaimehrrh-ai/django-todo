from django.urls import path
from . import views
from . import auth_views


urlpatterns=[


path('add/', views.add_task , name='add_page') ,
path('done/', views.check_task, name='boolpage'),
path('delete/', views.delete_task, name='delpage'),
path('edit/', views.edit_task, name='edpage'),
path('un_done/',views.undone_task, name='un_donepage'),
path('login/' , auth_views.log_in , name = 'login'),
path('sign_up/', auth_views.sign_up , name = 'sign_up' ),
path('', auth_views.sign_log , name='sign_log')





 ]
