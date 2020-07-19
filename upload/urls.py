from django.urls import path
from . import views

urlpatterns = [
    path('document_list', views.document_list, name='document_list'),
    path('upload_document', views.upload_document, name='upload_document'),
    path('delete_document/<int:pk>', views.delete_document, name='delete_document'),
] 