from django.db import models
from  django.contrib.auth.models import User

class Process(models.Model):
    """
    database table to define processes running on the server according
    to process id, process name and process owner (user).  It is not
    necessary for the process to be active or not.
    """
    
    pid   = models.IntegerField(default=0)   #process id according to os
    pname = models.CharField(max_length=200) #process name
    start = models.DateTimeField('date started',null=True)
    finish= models.DateTimeField('date ended',  null=True)
    status= models.CharField(max_length=200)
    active= models.BooleanField(default=False)

    def __str__(self):
        active={True:"running" , False:"stopped"}[self.active]
        returnStruct=dict(
            pid    =self.pid,
            pname  =self.pname,
            start  =self.start,
            finish =self.finish,
            active =active
            )
        returnString= """
\tThis is process %(pid)6d operating as:
\t\t%(pname)s 
\tThis process is: %(active)s
\tStarted: %(start)s
\tFinished:%(finish)s
        """%returnStruct
        return returnString

    #def __repr__(self):
    #    return str((self.pid, self.pname))

    def __call__(self):
        return self.pid
        

class ProcUser(models.Model):
    """
    form relational table beween processes and users
    """

    pid = models.ForeignKey( Process, on_delete=models.CASCADE)
    uid = models.ForeignKey( User )  ##uses the authenticated users
    #uid = models.IntegerField(default=0)   #user id according to db_table auth_user.  does not foreign key since this table is already defined

