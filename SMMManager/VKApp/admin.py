from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostItemAdmin(admin.ModelAdmin):
    pass

class ParserItemGroupsAdmin(admin.ModelAdmin):
    pass

class PublicPostAdmin(admin.ModelAdmin):
    pass




admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostItemAdmin)
admin.site.register(ParserItemGroups, ParserItemGroupsAdmin)
admin.site.register(PublicPost, PublicPostAdmin)