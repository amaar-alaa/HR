from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    
    path('addtodo/',addtodo,name='add_todo'),
    path('deleteTodoItem/<int:id>/',deleteTodoView,name='delete_todo'),
    path('checkTodoItem/<int:id>/',checkTodoView,name='check_todo'),
   
    path('', RepoList, name='repo_list'),
    path('<int:pk>/',RepoDetail.as_view(), name='repo_detail'),
    path('create/',RepoCreate.as_view() , name='repo_create'),
    path('edit/<int:id>', repo_edit, name='repo_edit'),
    path('update/<int:id>', repo_update, name='repo_update'),
    path('<int:pk>/',RepoCreate.as_view(), name='detail'),
    ##for reports
]