from django.contrib import admin

from .models import Page, Text, Revision

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'date']
	list_display = ('title', 'date')

admin.site.register(Page, PageAdmin)

class TextAdmin(admin.ModelAdmin):
	fields = ['body']

admin.site.register(Text, TextAdmin)

class RevisionAdmin(admin.ModelAdmin):
	fields = ['page', 'text', 'date']
	list_display = ('page', 'date', 'was_recent_revision')
	list_filter = ['date']
	
admin.site.register(Revision, RevisionAdmin)