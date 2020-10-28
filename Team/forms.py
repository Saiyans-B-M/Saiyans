from django import forms
from blog.models import Project,Article
from .models import UserProfile

class NewProjectForm(forms.ModelForm):
	pro = forms.IntegerField(widget=forms.HiddenInput(), initial=123)
	
	class Meta:
		model = Project
		fields = ['title','content','Functionality','remarks','ttl_img']
		# widgets = {'pro': forms.HiddenInput(),initial = 1}

class NewArticleForm(forms.ModelForm):
	art = forms.IntegerField(widget=forms.HiddenInput(), initial=123)

	class Meta:
		model = Article
		fields = ['title','content']
		# widgets = {'art': forms.HiddenInput(),initial = 1}

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ['pro_pic','full_name']

	# def clean_title(self,*args,**kwargs):
	# 	title = self.cleaned_data.get('title')
	# 	qs = Article.objects.filter(title__iexact = title)
	# 	if qs.exists():
	# 		raise forms.ValidationError('This title already exists')
	# 	return title