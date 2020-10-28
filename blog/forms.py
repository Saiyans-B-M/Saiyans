from django import forms
from .models import Subscriber,Application

class SubscriberForm(forms.ModelForm):

	class Meta:
		model = Subscriber
		fields = '__all__'

class NewApplicationForm(forms.ModelForm):

	class Meta:
		model = Application
		fields = '__all__'