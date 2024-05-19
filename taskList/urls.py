from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='taskList'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('createTask/', TaskCreate.as_view(), name='createTask'),
    path('updateTask/<int:pk>/', TaskUpdate.as_view(), name='updateTask'),
    path('deleteTask/<int:pk>/', DeleteView.as_view(), name='deleteTask'),
]
