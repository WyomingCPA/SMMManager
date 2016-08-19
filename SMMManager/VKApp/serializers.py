from .models import Post, Category, PublicPost, AdvertisingPost, HidePost
from django.contrib.auth.models import User

from rest_framework import serializers

class PostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'photo', 'time_parsing', 'category')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class PublicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPost
        
class AdvertisingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingPost

class HidePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HidePost