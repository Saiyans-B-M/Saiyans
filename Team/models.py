from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Message(models.Model):
	sender = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	msg_content = models.TextField()
	time = models.DateTimeField(auto_now_add = True)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	pro_pic = models.ImageField(upload_to = 'pro_pics/', default = 'pro_pics/default.png')
	full_name = models.CharField(max_length = 100)
	POSITION = [('MEMBER','MEMBER'),('TEAM LEADER','TEAM LEADER'),('SAIYANS LEADER','SAIYANS LEADER')]
	position = models.CharField(max_length = 20, choices = POSITION, default = 'mem')

	def __str__(self):  
          return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance) 

post_save.connect(create_user_profile, sender=User) 