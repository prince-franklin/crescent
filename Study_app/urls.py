from django.urls import path
from . import views



urlpatterns = [
    path('', views.crescent, name='crescent'),
    path('delete_task/<task_id>', views.delete_task, name='delete_task'),
    path('completed/<task_id>', views.completed, name='completed'),
    path('pending/<task_id>', views.pending, name='pending'),
    path('edit_task/<task_id>', views.edit_task, name='edit_task'),
    

]