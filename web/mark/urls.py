from django.conf.urls import url
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from .forms import EmailAuthenticationForm


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="mark/home.html"), name="home"),
    url(r'^login/$', login,
        {'template_name': 'mark/form_login.html',
         'authentication_form': EmailAuthenticationForm}, name='bookmark_login'),
    url(r'^logout/$', logout,
        {'template_name': 'mark/form_login.html'}, name='bookmark_logout'),
]