import todoapp.models
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http import HttpResponseRedirect
from django.contrib import messages


def home_page(request):
    if request.user.is_authenticated:
        contex = Todo.objects.all().values().order_by("-id").filter(user=request.user)
        return render(request, 'main_page.html', context={'items': contex})
    return render(request, 'main_page.html')


@csrf_exempt
def add_todo(request):
    time = timezone.now().date()
    text = request.POST['content']
    try:
        Todo.objects.create(user_id=request.user.id, user=request.user, title=text, added_date=time)
    except:
        messages.info(request, 'task can not be added', extra_tags='fail_to_add')
    return HttpResponseRedirect('/')


@csrf_exempt
def delete_todo(request, todo_id):
    try:
        Todo.objects.get(id=todo_id).delete()
    except todoapp.models.Todo.DoesNotExist:
        messages.info(request, 'task has been deleted or not exist', extra_tags='fail_to_delete')
    except:
        pass
    return HttpResponseRedirect('/')
