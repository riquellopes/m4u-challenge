from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

from mark.views import (
    CreateAccountView, BookmarkListView, BookmarkCreateView, BookmarkEditView, BookmarkDeleteView,
    UserListView)

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="mark/home.html"), name="home"),
    url(r'^login/$', login, {'template_name': 'mark/form_login.html'}, name='bookmark_login'),
    url(r'^logout/$', logout, {'template_name': 'mark/home.html'}, name='bookmark_logout'),
    url(r'^account/$', CreateAccountView.as_view(), name="account"),
    url(r'^users/$', UserListView.as_view(), name="users"),
    url(r'^bookmarks/$', BookmarkListView.as_view(), name="bookmarks"),
    url(r'^bookmarks/create$', BookmarkCreateView.as_view(), name="bookmarks_create"),
    url(r'^bookmarks/(?P<pk>\w+)$', BookmarkEditView.as_view(), name="bookmarks_updated"),
    url(r'^bookmarks/(?P<pk>\w+)/delete/', BookmarkDeleteView.as_view(), name="bookmarks_deleted"),
]
