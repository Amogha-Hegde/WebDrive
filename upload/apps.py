from django.apps import AppConfig
# from django.db.models.signals import post_save
# from django.dispatch import receiver
class UploadConfig(AppConfig):
    name = 'upload'

     
#     def ready(self):
#         from .models import Document
#         Document = self.get_model('Document')
#         post_save.connect(receiver,sender='upload.Document')