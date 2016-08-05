"""
Definition of urls for SMMManager.
"""


from django.contrib import admin
from datetime import datetime
from django.conf.urls import include
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from VKApp.api import PostView, CategoryView, PublicPostView



# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'GetPost', PostView)
router.register(r'GetCategory', CategoryView)
router.register(r'PublicPost', PublicPostView)

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),    
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
