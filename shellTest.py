
from django.http import HttpRequest
from django.test import Client, TestCase, RequestFactory
from django.contrib.sessions.backends.db import SessionStore

from traffic.views import index, loginOptional
from traffic.models import Process, ProcUser
from django.utils import timezone
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout



##test direct views in class and functions and get response
session_key='4gured3wido2wgv3kmdugl7i3745zijd'
user_session=SessionStore(session_key=session_key)# 
request=HttpRequest()
username = 'user01'
password = 'abc123'
user = authenticate(username=username, password=password)
request.user=user
request.session=user_session

view=index()
resp=view.get(request)
resp.status_code
resp.content

request.POST['username']=username
request.POST['password']=password
resp=view.post(request)
resp.status_code
resp.content

factory = RequestFactory()
##get anonymous login page
request = factory.get('/traffic/')
user=AnonymousUser()
request.user=user
response = loginOptional.as_view()(request)
response.content

#repeat for authenticated user
username = 'user01'
password = 'abc123'
user = authenticate(username=username, password=password)
request.user=user
response = loginOptional.as_view()(request)
response.content
