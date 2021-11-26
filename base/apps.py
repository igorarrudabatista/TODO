from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

class UserConfig(AppConfig):
     name = 'users'
     
     def ready(self):
         import users.signals   