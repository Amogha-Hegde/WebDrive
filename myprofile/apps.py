from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyprofileConfig(AppConfig):
    name = 'myprofile'
    
    def ready(self):
        from .models import Profile
        Profile = self.get_model('Profile')
        post_save.connect(receiver,sender='myprofile.Profile')