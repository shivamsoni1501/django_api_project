from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    data = [
        {'title': "First title", 'body': "First body"},
        {'title': "Second title", 'body': "Second body"},
        {'title': "Third title", 'body': "Third body"},
    ]
    return render(request, 'app1/index.html', {"content": data})

