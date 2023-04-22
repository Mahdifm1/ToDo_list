from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.http import HttpResponseRedirect


def home_page(request):
    return render(request, 'main_page.html')


@csrf_exempt
def add_todo(request):
    time = timezone.now()
    text = request.POST['content']
    Todo.objects.create(title=text, added_date=time)
    # print(request.POST)
    return HttpResponseRedirect('/')
