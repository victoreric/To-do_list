from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def delete(request, delete_id):
    List.objects.filter(id=delete_id).delete()
    return redirect('list:create')

def update(request, update_id):
    item_update = List.objects.get(id=update_id)
    data = {
        'item' : item_update.item,
        'completed' : item_update.completed,
    }

    item_form = ListForm(request.POST or None, initial = data, instance = item_update)

    if request.method == 'POST' :
        if item_form.is_valid():
            item_form.save()
        return redirect ('list:create')

    context = {
        'Title':'Update',
        "item_form" : item_form,
    }
    return render (request, 'list/update.html', context)

def create(request):
    all_items = List.objects.all()
    item_form = ListForm(request.POST or None)

    if request.method == 'POST' :
        if item_form.is_valid():
            item_form.save()
            return redirect ('list/create.html')

    context = {
        "Title" : 'Create',
        'all_items' : all_items,
        "item_form" : item_form,
    }
    return render (request, 'list/create.html', context)

def list(request):
    all_items = List.objects.all() 

    context = {
        'Title' : 'List',
        'all_items' : all_items,
    }
    return render (request, 'list/index.html', context)





'''
def index(request):
    if request.method =='POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has been added to list!'))
            return render (request,'list/index.html',{'all_items':all_items})
    else :
        all_items = List.objects.all
        return render(request, 'list/index.html',{'all_items': all_items})
'''