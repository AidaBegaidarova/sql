from . import views
from django.conf.urls import url
app_name = 'qa'
urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^login/$', views.test, name='login'),
    url(r'singup/$', views.test, name='signup'),
    url(r'question/(?P<id>\d+)/$', views.test, name='question'),
    url(r'ask/$', views.test, name='question'),
    url(r'popular/$', views.test, name='popular'),
    url(r'new/$', views.test, name='new'),
]