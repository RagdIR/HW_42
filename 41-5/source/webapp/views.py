from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def first_view(request):
    return render(request, 'first.html')

def second_view(request):
    return render(request, 'second.html')
