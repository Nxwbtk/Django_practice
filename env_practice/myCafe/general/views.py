from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def	first(request):
	template = loader.get_template('first.html')
	return HttpResponse(template.render())

def about(request):
	template = loader.get_template('about.html')
	return HttpResponse(template.render())