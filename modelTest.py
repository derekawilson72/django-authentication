from traffic.models import Process, ProcUser
from django.utils import timezone
from  django.contrib.auth.models import User
from django.contrib.auth import authenticate

##create a sample process
proc1=Process(pid=1, pname="sample proc", start = timezone.now(),
              active= True, status="serving as a sample process")
proc1.save()
proc2=Process(pid=2, pname="sample proc 2", start = timezone.now(),
              active= True, status="serving as another sample process")
proc2.save()

#query it
proc1=Process.objects.get(pid=1)  ##get the single object

#query an auth user (not admin)
user1=User.objects.get(username="user01")

##assign processes to user1
p1=ProcUser(pid=proc1, uid=user1)
p2=ProcUser(pid=proc2, uid=user1)
p1.save() 
p2.save()


##query processes assigned to user
user1=User.objects.get(username="user01")  ##get the single object
procs=ProcUser.objects.filter(uid=user1)   ##get many objects
##Authenticating users
user = authenticate(username='user01', password='abc123')



##create users
user2 = User()
user2.username='public enemy 1'
user2.save()
proc1=Process(pid=0, pname="sample public proc", start = timezone.now(),
              active= True, status="serving as a sample process in public")
proc2=Process(pid=0, pname="sample public proc 2", start = timezone.now(),
              active= True, status="serving as another public sample process")
proc1.save()
proc2.save()
p1=ProcUser(pid=proc1, uid=user2)
p2=ProcUser(pid=proc2, uid=user2)
p1.save() 
p2.save()
