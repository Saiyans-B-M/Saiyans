from django.urls import path,include,re_path
from .views import * 
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('',login_required(profile.as_view(),login_url = 'login'), name = 'profile'),
		re_path(r'delete_article/(?P<slug>[-\w]+)/$',delete_a,name = 'delete_article'),
		re_path(r'delete_project/(?P<slug>[-\w]+)/$',delete_p,name = 'delete_project'),
		re_path(r'edit_article/(?P<slug>[-\w]+)/$',edit_a,name = 'edit_article'),
		re_path(r'edit_project/(?P<slug>[-\w]+)/$',edit_p,name = 'edit_project'),
		re_path(r'edit_profile/',edit_profile,name = 'edit_profile'),

		url(r'^reset/$',
			auth_views.PasswordResetView.as_view(
				template_name='Team/password_reset.html',
				email_template_name='Team/password_reset_email.html',
				subject_template_name='Team/password_reset_subject.txt'
				),
			name='password_reset'),

		url(r'^reset/done/$',
			auth_views.PasswordResetDoneView.as_view(template_name='Team/password_reset_done.html'),
			name='password_reset_done'),

		url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
			auth_views.PasswordResetConfirmView.as_view(template_name='Team/password_reset_confirm.html'),
			name='password_reset_confirm'),

		url(r'^reset/complete/$',
			auth_views.PasswordResetCompleteView.as_view(template_name='Team/password_reset_complete.html'),
			name='password_reset_complete'),


		url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='Team/password_change.html'),
			name='password_change'),

		url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='Team/password_change_done.html'),
			name='password_change_done'),


]