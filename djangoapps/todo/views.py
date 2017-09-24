from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, HttpResponseBadRequest

from .models import Todo


# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todos': todo_list,
    }
    return render(request, 'index.html', context)


def append(request):
    todo = Todo(todo_text=request.POST['todo'])
    todo.save()
    return redirect('todo:index')


def delete(request):
    target_id = request.GET.get("id")
    if target_id is None:
        return HttpResponseBadRequest()
    try:
        target_id = int(target_id)
    except:
        return HttpResponseBadRequest()

    todo = get_object_or_404(Todo, id=target_id)
    todo.delete()

    return HttpResponse("Done")

