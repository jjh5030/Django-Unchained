from django.forms import ModelForm
from django import forms

from stories.models import Story
from django.contrib.auth.models import User


class StoryForm(ModelForm):
	class Meta:
		model = Story
		exclude = ('points', 'moderator','voters')

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.CharField(help_text="Please enter your email address.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password")

	class Meta:
		model = User
		fields = ['username','email','password']