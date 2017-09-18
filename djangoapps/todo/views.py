from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todos': todo_list,
    }
    return render(request, 'index.html', context)
