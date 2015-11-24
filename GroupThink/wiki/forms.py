from django import forms
from django.forms import ModelForm, Textarea

from .models import Page, Revision, Text

class PageForm(ModelForm):
	class Meta:
		model = Page
		fields = ['title']
		
class RevisionForm(ModelForm):
	class Meta:
		model = Revision
		fields = ['log']
		
class TextForm(ModelForm):
	class Meta:
		model = Text
		fields = ['body']