from .models import Todo

from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http import HttpResponseRedirect


def home_page(request):
    print(Todo.objects.all().values())
    contex = Todo.objects.all().values().order_by("added_date")
    return render(request, 'main_page.html', context={'items': contex})


@csrf_exempt
def add_todo(request):
    time = timezone.now().date()
    text = request.POST['content']
    Todo.objects.create(title=text, added_date=time)
    return HttpResponseRedirect('/')
