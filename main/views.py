from django.shortcuts import render
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
	todo_items = ToDo.objects.all().order_by("-added_date")
	return render(request,'main/index.html',{"todo_items":todo_items})

def add_todo(request):
	added_date = timezone.now()
	content = request.POST['content']
	ToDo.objects.create(added_date = added_date,text = content)
	return HttpResponseRedirect("/")

def delete_todo(request,todo_id):
	ToDo.objects.get(id=todo_id).delete()
	return HttpResponseRedirect('/')
