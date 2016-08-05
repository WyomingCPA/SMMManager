from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from VKApp.models import ParserItemGroups, Post
 
import vk_api

class Command(BaseCommand):
    help = 'Get Post'

    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        list_groups = ParserItemGroups.objects.all()
        for item in list_groups:
            self.getPostParser(item.idGroup, item.category)
      
    def getPostParser(self, idGroup, category):
         login, password = '+79210788944', '!@#Qwerty8344qwerty'
         vk_session = vk_api.VkApi(login, password, app_id = 4985624)

         try:
             vk_session.authorization()
         except vk_api.AuthorizationError as error_msg:
             print(error_msg)
             return

         tools = vk_api.VkTools(vk_session)

         wall = tools.get_all('wall.get', 100, {'owner_id': idGroup}, limit=100)
         for item in wall['items']:
             user = User.objects.get(pk = 1)
             try:
                 post = Post(category = category, text = str(item['text']), attachments = item['attachments'], user = user)
                 post.save()
             except:
                 pass


