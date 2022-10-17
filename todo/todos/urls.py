from django.urls import path
from .views import TodoListApiView, TodoDetailApiView
urlpatterns = [
    path("<int:pk>/", TodoDetailApiView.as_view(), name="todo_detail"),
    path("", TodoListApiView.as_view(), name="todo_list")
]
