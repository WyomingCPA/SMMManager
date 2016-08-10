# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
   
    def __unicode__(self):
        return self.name

#Модель поста
class Post(models.Model):
    category = models.ForeignKey(Category)
    text = models.CharField(max_length=2000)
    photo =  models.TextField()
    time_parsing = models.DateField(auto_now = True)

    def __unicode__(self):
        return self.text

#Модель групп для парсинга
class ParserItemGroups(models.Model):
    name = models.CharField(max_length = 100)
    idGroup = models.CharField(max_length=100)  
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.idGroup

#Модель опубликованного поста
class PublicPost(models.Model):
     user = models.ForeignKey(User)
     post_publick = models.ForeignKey(Post)

#Модель рекламмного поста
class AdvertisingPost(models.Model):
    user = models.ForeignKey(User)
    post_advert = models.ForeignKey(Post)