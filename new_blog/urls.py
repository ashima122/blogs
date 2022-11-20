from django.urls import path, include
from new_blog.views import * 

urlpatterns = [
    path('register',register),
    path('login', login_user, name='login_user'),
    path('', show, name='show'),
    path('Post-blog',file_new),  
    path('update/<int:id>', update),  
    path('edit/<int:id>', edit),  
    path('delete/<int:id>', destroy), 
    path('logout', logout_user, name='logout_user'),

]