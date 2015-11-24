from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /wiki/5/
    url(r'^(?P<page_id>[0-9]+)/$', views.article, name='article'),
    # ex: /wiki/5/edit/
    url(r'^(?P<page_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # ex: /wiki/5/revisions/
    url(r'^(?P<page_id>[0-9]+)/revisions/$', views.revisions, name='revisions'),
    # ex: /wiki/5/revert/2
    url(r'^(?P<page_id>[0-9]+)/revert/(?P<revision_id>[0-9]+)/$', views.revert, name='revert'),
]
