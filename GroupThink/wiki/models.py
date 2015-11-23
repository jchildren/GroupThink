from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=50)
	created_date = models.DateTimeField('date created')
	
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
	modified_date = models.DateTimeField('date modified')
	
	def __str__(self):
		return self.modified_date
		
	def was_recent_revision(self):
		return self.modified_date >= timezone.now() - datetime.timedelta(days=1)
