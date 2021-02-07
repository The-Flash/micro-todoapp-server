from django.urls import path

from . import views

urlpatterns = [
    path("todos/", views.TodoListCreateAPIView.as_view(), name="todos"),
    path("todos/<int:pk>/", views.TodoDetailAPIView.as_view(), name="todo"),
]