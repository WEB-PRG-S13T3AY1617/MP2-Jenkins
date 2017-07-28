from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^logout/$', views.logout, name = 'logout'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^register/submit/$', views.submit, name = 'submit'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^login/lsubmit/$', views.lsubmit, name = 'lsubmit'),
    url(r'^addpost/$', views.postnew, name = 'postnew'),
    url(r'^addpost/psubmit/$', views.psubmit, name = 'psubmit'),
    url(r'^(?P<post_id>[0-9]+)/$', views.postdetail, name = 'postdetail'),
    url(r'^(?P<user_username>[\w]+)/$', views.userdetail, name = 'userdetail'),
    url(r'^(?P<user_username>[\w]+)/allposts/$', views.userdetail, name = 'userdetail')
]