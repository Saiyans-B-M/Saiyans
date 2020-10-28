from django.urls import path,include,re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('',views.home_page, name = 'home_page'),
	re_path(r'^Project/(?P<slug>[-\w]+)/$',views.project,name = 'project'),
	re_path(r'^login/$',auth_views.LoginView.as_view(template_name = 'Team/login.html'),name = 'login'),
	re_path(r'^logout/$',auth_views.LogoutView.as_view(),name = 'logout'),
	re_path(r'^Articles/$',views.article,name = 'articles'),
	re_path(r'Articles/(?P<slug>[-\w]+)/$',views.read_article,name = 'read_article'),
	re_path(r'^JoinUs/$',views.join_us,name = 'join_us'),

]