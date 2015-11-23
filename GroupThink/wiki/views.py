from django.shortcuts import render
from django.http import HttpResponse

from .models import Revision

def index(request):
    latest_revisions_list = Revision.objects.order_by('-date')[:5]
    output = ', '.join([r.text.body for r in latest_revisions_list])
    return HttpResponse(output)
    
def page(request, page_id):
     return HttpResponse("You're looking at page %s." % page_id)
     
def edit(request, page_id):
    return HttpResponse("You're editing page %s." % page_id)

def revisions(request, page_id):
    return HttpResponse("You're looking at page %s revisions." % page_id)