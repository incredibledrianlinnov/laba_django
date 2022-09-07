from django.shortcuts import render

def index(request):
    return render(request, 'main/the_first.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def touch(request):
    return render(request, 'main/touch.html')