from .models import Post, Category, PublicPost
from django.contrib.auth.models import User

from rest_framework import serializers

class PostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #'attachments',
        fields = ('id', 'text', 'attachments', 'time_parsing', 'category')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class PublicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPost
        
