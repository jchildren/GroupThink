from django.contrib import admin

from .models import Page, Text, Revision

class TextAdmin(admin.ModelAdmin):
	fields = ['body']

admin.site.register(Text, TextAdmin)

class RevisionAdmin(admin.ModelAdmin):
	fields = ['text', 'date', 'user']
	list_display = ('date', 'was_recent_revision', 'user')
	list_filter = ['date']
	
admin.site.register(Revision, RevisionAdmin)

class PageAdmin(admin.ModelAdmin):
	fields = ['title', 'date', 'creator', 'latest', 'revisions']
	list_display = ('title', 'date', 'creator',  'latest')
	list_filter = ['date']

admin.site.register(Page, PageAdmin)