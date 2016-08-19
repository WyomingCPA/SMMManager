from django.conf.urls import url, include
from .api import PostView, CategoryView, PublicPostView, AdvertisingPostView, HidePostView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'GetPost', PostView, 'PostView')
router.register(r'GetCategory', CategoryView, 'CategoryView')
router.register(r'PublicPost', PublicPostView, 'PublicPostView')
router.register(r'AdvertPost', AdvertisingPostView, 'AdvertisingPostView')
router.register(r'HidePost', HidePostView, 'HidePostView')

urlpatterns = [
    url(r'^api/', include(router.urls)),
] 
