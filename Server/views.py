from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def article(request):
    return render(request,'article.html')

def news(request):
    return render(request,'news.html')

def CA(request):
    return render(request,'CA.html')

def messages(request):
    return render(request,'messages.html')