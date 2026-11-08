from django.db import models
from django.contrib.auth.models import User

class myuser(models.Model):

    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    
    def __str__(self):
      return  self.name

class tasks(models.Model):
    user =models.ForeignKey(myuser,null=True,on_delete=models.SET_NULL ,blank=True)
    task=models.CharField(max_length=100)
    due_date=models.DateField(null=True)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return  self.task
    
    
