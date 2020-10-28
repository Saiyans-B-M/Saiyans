from django.contrib import admin
from .models import Project,Subscriber,Article,Application
from Team.models import UserProfile	
# Register your models here.

admin.site.register(Project)
admin.site.register(Subscriber)
admin.site.register(Article)
admin.site.register(Application)
