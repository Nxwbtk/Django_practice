from django.shortcuts import render
from django.http import HttpResponse
from .models import Stock

# Create your views here.
def	hello(request):
	return render(request, 'hello.html', { 'name' : 'new'})

def	about(request):
	mycontext = {
		'name' : "New",
		'age' : "19",
		'name' : 'test',
		'age' : '20',
		'list' : [1, 2, 3, 4, 5],
	}
	return render(request, 'about.html', mycontext)

def	detail(request):
	obj = Stock.objects.get(id=2)
	context = {
		'id' : obj.id,
		'name': obj.name,
	}
	return render(request, "show/stcok_detail.html", context)
