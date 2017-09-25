from ask.qa.views import test
from django.conf.urls import url

urlpatterns = [
    url(r'^$', test, name='default'),
    url(r'^login/', test, name='login'),
    url(r'singup/', test, name='signup'),
    url(r'question/(?P<id>\d+)/', test, name='question'),
    url(r'ask/', test, name='question'),
    url(r'popular/', test, name='popular'),
    url(r'new/', test, name='new'),
]
