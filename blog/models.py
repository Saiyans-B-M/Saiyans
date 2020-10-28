from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.utils import timezone	
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

import string 
from django.utils.text import slugify 
import random 

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length = 255)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	Functionality = models.TextField(null = True, blank = True, default = 'Not Mentioned')
	remarks = models.TextField()
	ttl_img = models.ImageField(upload_to = 'images/')
	created_on = models.DateTimeField(auto_now_add = True)
	slug = models.SlugField(null = True)

class Subscriber(models.Model):
	email = models.CharField(max_length = 255, null = True, blank = True)

class Article(models.Model):
	title = models.CharField(max_length = 255)
	content = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	created_on = models.DateTimeField(auto_now_add = True)
	slug = models.SlugField(null = True)

class Application(models.Model):
	EDUCATION = [('scholar','SCHOLAR'),('fresher','FRESHER')]
	username = models.CharField(max_length = 55,help_text = 'This will be your username, you cannot change it later')
	email = models.CharField(max_length = 255, null = True, blank = True)
	phone = PhoneNumberField(help_text = 'please enter along with your country code. e.g "+91"')
	status = models.CharField(max_length = 10,choices = EDUCATION, default = 'scholar')
	About = models.TextField(help_text = 'say something about you, you can leave it empty too')

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 

def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.title) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = Project) 
pre_save.connect(pre_save_receiver, sender = Article) 