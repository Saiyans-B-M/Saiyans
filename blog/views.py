from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Project,Article
from .forms import SubscriberForm, NewApplicationForm
from django.core import serializers

# Create your views here.


def home_page(request):
	template = "blog/home.html"
	try:
		projects = Project.objects.filter()
	except:
		projects = 'none'
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid:
			form.save()

	# projects = Project.Objects.all()
	
	# if request.is_ajax() and request.method == 'POST':
	# 	form = SubscriberForm(request.POST)
	# 	if form.is_valid:
	# 		instance = form.save()
	# 		# ser_instance = serializers.serialize('json', [ instance, ])
	# 		return JsonResponse(status=200)
	# 	else:
	# 		return JsonResponse({"error": form.errors}, status=400)	
			# return render(request,template,{'projects' : projects,'form':form})

	form = SubscriberForm()
	# return HttpResponse("<h1>This is home page</h1>")
	return render(request,template,{'projects' : projects,'form':form})

# def save_subscribe(request):
# 	if request.is_ajax() and request.method == 'POST':
# 		return JsonResponse(status = 200)
# 	else:
# 		return JsonResponse({"error":form.errors})


def project(request,slug):
	template = 'blog/projects.html'

	obj = get_object_or_404(Project,slug = slug)
	return render(request,template,{'projects':obj})

def article(request):
	template = 'blog/articles.html'
	obj = get_list_or_404(Article)
	return render(request,template,{'articles':obj})

def read_article(request,slug):
	template = 'blog/read_article.html'
	obj = get_object_or_404(Article,slug = slug)
	return render(request,template,{'article':obj})

def join_us(request):
	template = 'blog/join_us.html'
	if request.method == 'POST':
		form = NewApplicationForm(request.POST)
		if form.is_valid:
			form.save()
			
	form = NewApplicationForm
	return render(request,template,{'form' : form})