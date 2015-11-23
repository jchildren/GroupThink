from django.db import models

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=50)
	created_date = models.DateTimeField('date created')
	page_latest = models.OneToOneField(Revision)
	
class Revision(models.Model)
	rev_page = models.ForeignKey(Page)
	rev_text = models.OneToOneField(Text)
	modified_date = models.DateTimeField('date modified')

class Text(models.Model):
	body = models.CharField(max_length=5000)
	