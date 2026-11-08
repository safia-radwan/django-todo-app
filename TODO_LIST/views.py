import django
from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from .forms import date_Form, register_from
from .models import * 
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login as mylogin ,logout
# Create your views here.


@login_required(login_url="login")
def home(request)  :
     current_user=get_object_or_404(myuser,user=request.user)
     task2=tasks.objects.filter(user=current_user)
     
     
     if request.method =='POST':
          task_id=request.POST.get('task_id')
          if task_id :
               task= tasks.objects.get(id=task_id)
               form=date_Form(request.POST,instance=task)
               form.save()
               form=date_Form()
          else :     
               form = date_Form(request.POST)
               
               if form.is_valid():
                    new_task=form.save(commit=False)
                    new_task.user=current_user
                    new_task.save()
                    return  redirect ('home')
                    
                    
     else:
          form=date_Form()
               
         
     return render(request,'home.html',{'form':form ,'tasks':task2})
     
     
     
     
     
def change_task(request,task_id):
     task=get_object_or_404(tasks,id=task_id)
     task.is_completed= not task.is_completed
     print(task)
     print(task.is_completed)
     task.save()
     return  redirect ('home')
     print(task.is_completed)

def delete_task(request,task_id):
     task=get_object_or_404(tasks,id=task_id)
     task.delete()
     return  redirect ('home')



def completed(request):
     
     completed_tasks=tasks.objects.filter(is_completed=True,user__user=request.user)
     return render(request,'completed.html',{'tasks':completed_tasks})


def edit(request,task_id):
     task=get_object_or_404(tasks,id=task_id)
     form = date_Form(instance=task)
     if request.method =='POST':
          form = date_Form(request.POST,instance=task)
          if form.is_valid():
               form.save()
               return  redirect ('home')
               
               
     else:
          form=date_Form(instance=task)
               
         
     return render(request,'home.html',{'form':form ,'tasks':task})
      
          




def register(request):
     form = register_from()
     if request.method =='POST':
          form = register_from(request.POST)
          if form.is_valid():              
               user=form.save()
               myuser.objects.create(user=user,name=user.username)
               return redirect('login')
     
     return render(request,'register.html',{'form':form})

def login(request):
    
     if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(request,username=username,password=password)
          if user is not None:
               mylogin(request,user)
               return redirect('home')
          else:
               messages.info(request,'credentail error')  
     return render(request,'login.html',{})          
               
def user_logout(request):
     logout(request)
     return redirect ('login')