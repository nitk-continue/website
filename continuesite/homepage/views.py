from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context={}
    return render(request, 'homepage/index.html', context)

def category(request):
    context={}
    return render(request,'homepage/category.html',context)

def about(request):
    context={}
    return render(request,'homepage/about.html',context)
    
def contact(request):
    context={}
    return render(request,'homepage/contact.html',context)

def text_post(request):
    context={}
    return render(request,'homepage/text-post-standard.html',context)
    
    