from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register/', views.register, name = 'register'),
   # url(r'^register/submit', views.submit, name = 'submit'),
    url(r'^(?P<post_id>[0-9]+)/$', views.postdetail, name = 'postdetail'),
    url(r'^(?P<user_username>[\w]+)/$', views.userdetail, name = 'userdetail')
]