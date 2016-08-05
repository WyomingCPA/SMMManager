from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from serializers import PostItemSerializer, CategorySerializer, PublicPostSerializer
from datetime import datetime    
from .models import Post, Category, PublicPost
from accounts.models import CustomProfile


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class =PostItemSerializer
    http_method_names = ['get',] 
    
    def get_queryset(self):                
        category_id = self.request.GET['category'] 
        category=Category.objects.get(id = category_id)
        public_post = PublicPost.objects.filter(user=self.request.user).values('post_publick')
        result =  Post.objects.exclude(id__in=public_post)
                
        return result

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PublicPostView(viewsets.ModelViewSet):
    queryset = PublicPost.objects.all()
    serializer_class = PublicPostSerializer
    #http_method_names = ['post',] 

