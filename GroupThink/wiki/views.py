import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Page, Revision, Text
from .forms import PageForm, RevisionForm, TextForm

def index(request):
    latest_pages_list = Page.objects.order_by('-date')[:5]
    template = loader.get_template('pages/index.html')
    context = {'latest_pages_list': latest_pages_list}
    return render(request, 'pages/index.html', context)
    
def article(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'pages/article.html', {'page': page})
     
def edit(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
        
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        page_form = PageForm(request.POST)
        revision_form = RevisionForm(request.POST)
        text_form = TextForm(request.POST)
        
        # check whether it's valid:
        if page_form.is_valid() and revision_form.is_valid() and text_form.is_valid():
        
            # Creates a new text object with the form input
            text = Text(body=text_form.cleaned_data['body'])
            text.save()
            
            #TODO: correctly access user
            user = User.objects.get(id=1)
            
            # Creates a new revision with the updated text
            revision = Revision(text=text, date=timezone.now(), log=revision_form.cleaned_data['log'], user=user)
            revision.save()
        
            # Updates this revision to the latest
            page.title = page_form.cleaned_data['title']
            page.latest = revision
            page.revisions.add(revision)
            page.save()
            
            # process the data in form.cleaned_data as required
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('wiki:article', args=(page.id,)))
        else:
            return render(request, 'pages/article.html', {'page': page})

    # if a GET (or any other method) we'll create a blank form
    else:
        page_form = PageForm(instance=page)
        revision_form = RevisionForm()
        text_form = TextForm(instance=page.latest.text)
        
        return render(request, 'pages/edit.html', 
        {'page': page,
         'page_form': page_form,
         'revision_form': revision_form,
         'text_form': text_form,
         })

def revisions(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'pages/revisions.html', {'page': page})
    
def revert(request, page_id, revision_id):
    page = get_object_or_404(Page, pk=page_id)
    revision = get_object_or_404(Revision, pk=revision_id)
    
    if page.latest.text == revision.text:
        # TODO: Display an error
        error_message = 'Target revision identical to current'
        
        return HttpResponseRedirect(reverse('wiki:revisions', args=(page.id,)))
    
    else:
        # Default log message for reversion
        log_message = 'Reverted to ' + revision.date.strftime('%c')
    
        user = User.objects.get(id=1)
        user.save()
    
        new_revision = Revision(text=revision.text, date=timezone.now(), log=log_message, user=user)
        new_revision.save()
        
        page.latest = new_revision
        page.save()
        page.revisions.add(new_revision)
    
        return HttpResponseRedirect(reverse('wiki:revisions', args=(page.id,)))