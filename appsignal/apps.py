from unicodedata import name
from django.apps import AppConfig


class AppsignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appsignal'

    #config signal

    def ready(self):
        import  appsignal.signals      #now go to __init__
