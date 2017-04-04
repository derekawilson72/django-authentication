from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^login/$', 
        auth_views.login, 
        {'template_name': 'login.html',
         },
        name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'validate', views.validate, name='validate'),

    url(r'public', views.loginOptional.as_view(), name='public'),
  

]
