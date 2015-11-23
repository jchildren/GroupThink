import datetime

from django.db import models
from django.utils import timezone

class Page(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateTimeField('date created')
	
	def __str__(self):
		return self.title
	
	pass
	
class Text(models.Model):
	body = models.CharField(max_length=5000)
	
	def __str__(self):
		return self.body
		
	pass
	
class Revision(models.Model):
	page = models.ForeignKey(Page)
	text = models.OneToOneField(Text)
	date = models.DateTimeField('date modified')
	
	def __str__(self):
		return self.date.strftime('%c')
		
	def was_recent_revision(self):
		return self.date >= timezone.now() - datetime.timedelta(days=1)
