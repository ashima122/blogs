from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.contrib.auth.models import User
from new_blog.models import *
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
import datetime
#Register API
class RegisterApi(APIView):
    def post(self, request, *args,  **kwargs):
        serializer = RegisterSerializer(data=request.data)
        print(request.data['username'])
        if serializer.is_valid():
            username = request.data['username']
            password = request.data['password']
            profile_pic = request.data['profile_pic']
            new_user =User.objects.create(username=username,password=make_password(password))
            profile.objects.create(user_id=new_user.id,profile_pic=profile_pic)
        
            return Response({
                "message": "User Created Successfully",
            })
        return Response({
                "message": "User Not Created Successfully",
            })

class AddBlogApi(APIView):
     permission_classes = [IsAuthenticated]
     def post(self, request, *args,  **kwargs):
        serializer = PostBlogSerializer(data=request.data)
 
        if serializer.is_valid():
            title = request.data['title']
            content = request.data['content']
            blog.objects.create(title=title,content=content,user=request.user)
        
            return Response({
                "message": "Blog Created Successfully",
            })
        return Response({
                "message": "Blog Not Created Successfully",
            })

class GetBlogApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args,  **kwargs):
        blogs = blog.objects.all().order_by('-id')  
        serializer = GetBlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
class GetIdBlogApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,id, *args,  **kwargs):
        blogs = blog.objects.get(id=id)  
        serializer = GetBlogSerializer(blogs)
        return Response(serializer.data)

class UpdateBlogApi(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request,id, *args,  **kwargs):
        blogs = blog.objects.get(id=id) 
        print(request.user)
        print(blogs.user)
        if request.user == blogs.user:
            serializer = PostBlogSerializer(data=request.data)
            if serializer.is_valid():
                title = request.data['title']
                content = request.data['content']
                blogs.title=title
                blogs.content=content
                now=datetime.datetime.now()
                blogs.updated_date=  now.strftime("%Y-%m-%d")
                blogs.save()  
            
                return Response({
                    "message": "Blog updated Successfully",
                })
            return Response({
                    "message": "Blog Not updated Successfully",
                })
        return Response({
                    "message": "You cann't have permission to update this blog",
                })


class DeleteBlogApi(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request,id, *args,  **kwargs):
        blogs = blog.objects.get(id=id)  
        if request.user == blogs.user_id:
            blogs.delete()
            return Response({
                    "message": "Blog deleted Successfully",
                }) 
        return Response({
                    "message": "You cann't have permission to delete this blog",
                })