from django.urls import path
from .views import todo, todo_detail

urlpatterns = [
    path('todo/', todo),
    path('todo/detail/<int:id>/', todo_detail),
]