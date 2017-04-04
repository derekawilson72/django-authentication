from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout, forms 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response


from traffic.models import Process, ProcUser
from traffic.negotiation import IgnoreClientContentNegotiation

class loginOptional(View):
    """
    Public access view which will render user information page if logged in 
    or publicly accessible information if not logged in.
    """
    def get(self, request, *args, **kwargs):
        user=request.user
        #print user
        if user.is_authenticated:
            request.session.marker='user wants a login session'
            return index.as_view()(request)
        else:
            request.session.marker='user wants anonymous session'
            return genericTable.as_view()(request)



class genericTable(APIView):
    """
    Public table showing publicly accessible information.   The anonymous:True
    key will show the login form for future login access.
    """
    
    def get(self, request, *args, **kwargs):
        user=User.objects.get(username='public enemy 1')
        procs=ProcUser.objects.filter(uid=user)     ##get many objects
        form=forms.AuthenticationForm()
        procList=[{'pname':proc.pid.pname, 'last_name':proc.uid.last_name, 'pid':proc.pid.pid} for proc in procs]
        retString="%s\n%s"%(user,str(procs))
        #return HttpResponse("Hello, world. You're at the traffic index.%s"%user)
       
        userHeading="This is public page"
        context={'user': userHeading, 
                 'procs': procList, 
                 'form': form,
                 'anonymous':True}
        
        return render(request,'index.html',context)


class index(LoginRequiredMixin, View):
    template_name = "index.html"   
    login_url = 'public'
    # redirect_field_name=''
    

    #@login_required(login_url='/traffic/login')
    def get(self, request, *args, **kwargs):
        user=request.user
        procs=ProcUser.objects.filter(uid=user)   ##get many objects
        procList=[{'pname':proc.pid.pname, 'last_name':proc.uid.last_name, 'pid':proc.pid.pid} for proc in procs]
        retString="%s\n%s"%(user,str(procs))
        #return HttpResponse("Hello, world. You're at the traffic index.%s"%user)
       
        context={'user': user, 'procs': procList}
        return render(request,'index.html',context)

    def post(self, request, *args, **kwargs):
        """
        Posting operation 
        """
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print('# Redirect to a success page.')
                yourInfo={'a':1, 'b': 2}
                return JsonResponse(yourInfo)
            else:
                print('# Return a disabled account error message')
                # ...
                yourInfo={'a':'invalid login', 'b': None}
                return JsonResponse(yourInfo)
        else:
            print('# Return an invalid login error message.')
        yourInfo={'a':'You are not logged in.', 'b': None}
        return JsonResponse(yourInfo)



    
#@login_required(login_url='/traffic/login')
def validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print('# Redirect to a success page.')
            return HttpResponseRedirect('/traffic')
        else:
            print('# Return a disabled account error message')
            #...
    else:
        print('# Return an invalid login error message.')
    return HttpResponse("You are not logged in.")
    #


