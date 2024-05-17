from django.urls import path
from . import views
urlpatterns = [
    path('submit-the-task-solution/<int:task_id>/', views.StudentFormView, name='solution'),
    path('', views.TaskFormView, name='task'),
]