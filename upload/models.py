from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

def get_upload_path(instance, filename):
    return os.path.join('documents', instance.user.username, filename)

class Document(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    title=models.CharField(max_length=100)
    file = models.FileField(upload_to=get_upload_path)
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

