from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskComplete, TaskListCompleted

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('task-complete/<int:pk>/', TaskComplete.as_view(), name='task-complete'),
    path('task-list-completed', TaskListCompleted.as_view(), name='task-list-completed')

]
