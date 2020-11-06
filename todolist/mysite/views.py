from django.shortcuts import render

def index(request):
    context = {
        'Title' : 'Home'
    }
    return render(request,'index.html', context)