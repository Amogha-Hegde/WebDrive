from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import DocumentForm
from upload.models import Document

def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request,'upload/document_list.html',{
        'documents': documents

    })



def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
           doc=form.save(commit=False)#commit=False tells Django that "Don't send this to database yet, I have more things I want to do with it."
           doc.user=request.user
           doc.save()                                     
           return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request,'upload/upload_document.html',{
        'form':form  
    })

def delete_document(request,pk):
    if request.method =='POST':
        document = Document.objects.get(pk=pk)
        document.delete()
    return redirect('document_list')




  

