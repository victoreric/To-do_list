from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.db.models import Q
from django.contrib import messages

def cross_off (request,list_id):
    item= List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('list:index')

def uncross(request, list_id):
    item= List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('list:index')

def search(request):
    queryList = List.objects.all()
    queryCari = request.GET.get('kolomCari')

    if queryCari !='' and queryCari is not None :
        queryList = queryList.filter(Q(item__icontains = queryCari))

    context = {
        'Title' : 'Search',
        'queryset' : queryList,
        }
    return render(request, 'list/search.html', context)

def delete(request, delete_id):
    List.objects.filter(id=delete_id).delete()
    messages.success(request,('Item has been Deleted..!'))
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
            messages.success(request,('Item has been edited..!'))
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
            messages.success(request,('Item has been added to list!'))
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