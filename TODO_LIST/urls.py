from django.urls import path
from . import views
urlpatterns = [
   path('',views.home ,name='home'),
   path('change_task/<int:task_id>/',views.change_task, name='change_task'),
   path('delete_task/<int:task_id>/',views.delete_task, name='delete_task'),
   path('edit/<int:task_id>/',views.edit, name='edit'),
   
   path('completed',views.completed, name="completed"),
   path('register',views.register, name="register"),
   path('login',views.login, name="login"),
   path('logout',views.user_logout, name="logout"),
   
   
   
   
   
]
