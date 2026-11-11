from django.db import models
from django.contrib.auth.models import User

class myuser(models.Model):

    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
      return  self.name

class tasks(models.Model):
    Priority=[('High','High'),('Medium','Medium'),('Low','Low')]
    Catigory=[('Work','Work'),('Personal','Personal'),('Study','Study')]
    user =models.ForeignKey(myuser,null=True,on_delete=models.SET_NULL ,blank=True)
    task=models.CharField(max_length=100)
    due_date=models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    priority=models.CharField(choices=Priority,default='Low',max_length=10)
    catigory=models.CharField(choices=Catigory,default='Personal',max_length=10)
    
    def __str__(self):
        return  self.task
    
    
