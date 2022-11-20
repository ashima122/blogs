from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
      path('register', RegisterApi.as_view()),
      path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      path('add-blog', AddBlogApi.as_view()),
      path('get-blog', GetBlogApi.as_view()),
      path('get-id-blog/<int:id>', GetIdBlogApi.as_view()),
      path('update-blog/<int:id>', UpdateBlogApi.as_view()),
      path('delete-blog/<int:id>', DeleteBlogApi.as_view())
]