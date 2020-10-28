from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from blog.models import Project,Article
from django.conf import settings
from .forms import NewProjectForm,NewArticleForm,UserProfileForm
from django.views import View
from .models import Message, UserProfile

# Create your views here.

# @login_required(login_url = 'login')
# 	@cache_control(no_cache=True, must_revalidate=True)
class profile(View):

	def get(self,request):
		template = 'Team/profile.html'
		try:
			projects = Project.objects.filter(author = request.user)
		except:
			projects = 'none'
		try:
			articles = Article.objects.filter(author = request.user)
		except:
			articles = 'none'
		profile = get_object_or_404(UserProfile, user = request.user)
		project_form = NewProjectForm()
		article_form = NewArticleForm()
		return render(request,template,{'projects':projects,'articles':articles,'p_form':project_form,'a_form':article_form, 'profile' : profile})

	def post(self,request):
			
		if request.POST.get('pro'):
			template = 'Team/success_page.html'
			form = NewProjectForm(request.POST,request.FILES)
			if form.is_valid:
				var = form.save(commit = False)
				var.author = request.user
				# var.ttl_img = request.FILES['ttl_img']
				var.save()
				msg = 'Succesfully posted a new project named '
				return render(request,template,{'obj' : var,'msg':msg})
		elif request.POST.get('art'):
			template = 'Team/success_page.html'
			form = NewArticleForm(request.POST)
			if form.is_valid:
				var = form.save(commit = False)
				var.author = request.user
				var.save()
				msg = 'Succesfully posted a new article named '
				return render(request,template,{'obj' : var,'msg':msg})
		template = 'Team/profile.html'		
		project_form = NewProjectForm()
		article_form = NewArticleForm()
		try:
			projects = Project.objects.filter(author = request.user)
		except:
			projects = 'none'
		try:
			articles = Article.objects.filter(author = request.user)
		except:
			articles = 'none'
		# messages = get_list_or_404(Message)
		return render(request,template,{'projects':projects,'articles':articles,'p_form':project_form,'a_form':article_form,'editing': False})

@login_required(login_url = 'login')
def delete_a(request,slug):
	template = 'Team/success_page.html'
	obj = get_object_or_404(Article,slug = slug)
	obj.delete()
	msg = 'Succesfully deleted the article '
	return render(request,template,{'obj' : obj,'msg':msg})
	# return HttpResponse('<h2>lets delete page of article</h2>')

@login_required(login_url = 'login')
def delete_p(request,slug):
	template = 'Team/success_page.html'
	obj = get_object_or_404(Project,slug = slug)
	obj.delete()
	msg = 'Succesfully deleted the Project'
	return render(request,template,{'obj' : obj,'msg':msg})
	# return HttpResponse('<h2>lets delete page of project</h2>')

def edit_a(request,slug):
	obj = get_object_or_404(Article,slug = slug)
	if request.method == 'POST':
		form = NewArticleForm(request.POST,request.FILES,instance = obj)
		if form.is_valid:
			var = form.save(commit = False)
			# var.author = request.user
			var.save()
		msg = 'Succesfully edited the article'	
		template = 'Team/success_page.html'
		return render(request,template,{'obj' : obj, 'msg':msg})

	
	template = 'Team/profile.html'
	project_form = NewProjectForm()
	article_form = NewArticleForm(instance = obj)
	projects = get_list_or_404(Project,author = request.user)
	articles = get_list_or_404(Article,author = request.user)
	# messages = get_list_or_404(Message)
	profile = get_object_or_404(UserProfile, user = request.user)
	return render(request,template,{'projects':projects,'articles':articles,'profile':profile,'p_form':project_form,'a_form':article_form,'editing':True})

def edit_p(request,slug):
	obj = get_object_or_404(Project,slug = slug)
	template = 'Team/profile.html'
	if request.method == 'POST':
		form = NewProjectForm(request.POST,request.FILES,instance = obj)
		if form.is_valid:
			var = form.save()
			# var.author = request.user
			# var.save()
		msg = 'Succesfully edited the article'	
		template = 'Team/success_page.html'
		return render(request,template,{'obj' : obj,'msg':msg})

	
	
	project_form = NewProjectForm(instance = obj)
	article_form = NewArticleForm()
	projects = get_list_or_404(Project,author = request.user)
	articles = get_list_or_404(Article,author = request.user)
	# messages = get_list_or_404(Message)
	profile = get_object_or_404(UserProfile, user = request.user)
	return render(request,template,{'projects':projects,'articles':articles,'profile':profile,'p_form':project_form,'a_form':article_form,'editing':True})

def edit_profile(request):
	u = request.user
	obj = get_object_or_404(UserProfile, user = u)
	template = 'Team/edit_profile.html'
	if request.method == 'POST':
		form = UserProfileForm(request.POST,request.FILES,instance = obj)
		if form.is_valid:
			var = form.save()
			# var.author = request.user
			# var.save()
		msg = 'Succesfully Updated the profile'	
		template = 'Team/success_page.html'
		return render(request,template,{'obj' : obj, 'msg':msg})

	form = UserProfileForm(instance = obj)
	return render(request,template,{'form':form})
