from django.contrib import admin
from .models import *

# Register your models here.

class BlogtTableAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'content', 'profile', 'created_date','updated_date','user']
admin.site.register(blog, BlogtTableAdmin)

class ProfileTableAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'profile_pic']
admin.site.register(profile, ProfileTableAdmin)