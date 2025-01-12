from django.shortcuts import render

from .models import Todo

def todo_list(resquest):
   # todos =Todo.objects.all()
    nome = "Ana"
    return render(resquest, "todos/todo_list.html", {"nome": nome}) 