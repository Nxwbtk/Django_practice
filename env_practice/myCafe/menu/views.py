from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def	menu_list(request):
	template = loader.get_template('Menu.html')
	return HttpResponse(template.render())

def	one_item(request):
	return HttpResponse("One Item")