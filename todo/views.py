from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets, permissions
from todo.serializers import TodoSerializer
from todo.models import Todo

# Html / Htmx Views.

def todos(request):
    todos = Todo.objects.order_by('-created_at')
    return render(request, 'todolist.html', {'todos': todos})

def todos_get(request):
    todos = Todo.objects.order_by('-created_at')
    if(request.GET.get('status')): 
        status = request.GET['status']
        todos = todos.filter(status=status)
    return render(request, 'todolist_x.html', {'todos': todos})


def todo_add(request):
    if request.method == "POST":
        name = request.POST['name']
        if name :
            todo = Todo.objects.create(name=name)
            todo.save()
    todos = Todo.objects.order_by('-created_at')
    return render(request, 'todolist_x.html', {'todos': todos})

def todo_toggle(request):
    if request.method == "POST":
        todo_id = request.POST['id']
        todo = Todo.objects.get(pk=todo_id)
        todo.status = not todo.status 
        todo.save()
    todos = Todo.objects.order_by('-created_at')
    return render(request, 'todolist_x.html', {'todos': todos})


def todo_delete(request):
    if request.method == "POST":
        todo_id = request.POST['id']
        todo = Todo.objects.get(pk=todo_id)
        todo.delete() 
    todos = Todo.objects.order_by('-created_at')
    return render(request, 'todolist_x.html', {'todos': todos})


# REST Views.

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
